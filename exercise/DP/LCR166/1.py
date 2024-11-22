from typing import List


class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        m, n = len(frame), len(frame[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = frame[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + frame[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + frame[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + frame[i][j]
        return dp[m - 1][n - 1]
        