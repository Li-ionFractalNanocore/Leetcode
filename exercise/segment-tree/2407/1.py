from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        st = [0] * (2 << max_num.bit_length())

        def modify(idx, val, length, l, r):
            if l == r:
                st[idx] = length
                return
            m = (l + r) >> 1
            if val <= m:
                modify(idx * 2, val, length, l, m)
            else:
                modify(idx * 2 + 1, val, length, m + 1, r)
            st[idx] = max(st[idx * 2], st[idx * 2 + 1])

        def query(idx, l, r, ql, qr):
            if qr < l or r < ql:
                return 0
            if ql <= l and r <= qr:
                return st[idx]
            m = (l + r) >> 1
            return max(query(idx * 2, l, m, ql, qr), query(idx * 2 + 1, m + 1, r, ql, qr))

        result = 0
        for num in nums:
            before = num - k
            l = query(1, 0, max_num, before, num - 1) + 1
            result = max(result, l)
            modify(1, num, l, 0, max_num)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([1, 100, 500, 100000, 100000], 100000))