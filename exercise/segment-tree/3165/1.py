from typing import List


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        st = [[0] * 4 for _ in range(2 << n.bit_length())]

        def update(idx, i, val, l, r):
            if l == r:
                st[idx][3] = max(val, 0)
                return

            m = (l + r) // 2
            if i <= m:
                update(idx * 2, i, val, l, m)
            else:
                update(idx * 2 + 1, i, val, m + 1, r)
            st[idx][0] = max(st[idx * 2][1] + st[idx * 2 + 1][0], st[idx * 2][0] + st[idx * 2 + 1][2])
            st[idx][1] = max(st[idx * 2][0] + st[idx * 2 + 1][3], st[idx * 2][1] + st[idx * 2 + 1][1])
            st[idx][2] = max(st[idx * 2][2] + st[idx * 2 + 1][2], st[idx * 2][3] + st[idx * 2 + 1][0])
            st[idx][3] = max(st[idx * 2][2] + st[idx * 2 + 1][3], st[idx * 2][3] + st[idx * 2 + 1][1])

        for i, num in enumerate(nums):
            update(1, i, num, 0, n - 1)

        result = 0
        for i, val in queries:
            update(1, i, val, 0, n - 1)
            result = (result + st[1][3]) % MOD

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSumSubsequence([3,5,9], [[1,-2],[0,-3]]))



        