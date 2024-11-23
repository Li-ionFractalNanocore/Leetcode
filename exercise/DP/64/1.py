from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        for i in range(m):
            for j in range(n):
                dp[j+1] = min(dp[j], dp[j+1]) + grid[i][j]
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum([[1, 2], [1, 1]]))  # 3
    print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7