from typing import List


class Node:
    def __init__(self):
        self.reversed = False
        self.num1_sum = 0

    def __repr__(self):
        return f"Node({self.reversed}, {self.num1_sum})"


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        st = [Node() for _ in range(2 << n.bit_length())]

        def reverse(idx, l, r, ql, qr):
            if l > qr or r < ql:
                return
            if ql <= l and r <= qr:
                if l == r:
                    st[idx].num1_sum = 1 - st[idx].num1_sum
                else:
                    st[idx].reversed ^= True
                    st[idx].num1_sum = r - l + 1 - st[idx].num1_sum
            else:
                m = (l + r) >> 1
                if st[idx].reversed:
                    reverse(idx << 1, l, m, l, m)
                    reverse(idx << 1 | 1, m + 1, r, m + 1, r)
                    st[idx].reversed = False
                reverse(idx << 1, l, m, ql, qr)
                reverse(idx << 1 | 1, m + 1, r, ql, qr)
                st[idx].num1_sum = st[idx << 1].num1_sum + st[idx << 1 | 1].num1_sum

        for i, num in enumerate(nums1):
            if num == 1:
                reverse(1, 0, n - 1, i, i)

        nums2_sum = sum(nums2)
        results = []
        for op, l, r in queries:
            if op == 1:
                reverse(1, 0, n - 1, l, r)
            elif op == 2:
                nums2_sum += st[1].num1_sum * l
            else:
                results.append(nums2_sum)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.handleQuery([1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]])) # [3]
        