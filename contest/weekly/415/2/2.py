from typing import List
from functools import cache


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        m, n = len(a), len(b)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for j in range(n):
            dp[0][j] = max(a[0] * b[j], dp[0][j-1])

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = max(dp[i-1][j-1] + a[i] * b[j], dp[i][j-1])

        return dp[m-1][n-1]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore([-1,4,5,-2], [-5,-1,-3,-2,-4]))  # -1
    print(solution.maxScore([3,2,5,6], [2,-6,4,-5,-3,2,-7]))  # 26
