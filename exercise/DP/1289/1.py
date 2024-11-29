from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [num for num in grid[0]]

        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                new_dp[j] = grid[i][j] + min(dp[0:j] + dp[j+1:])
            dp = new_dp
        return min(dp)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))  # 13
        