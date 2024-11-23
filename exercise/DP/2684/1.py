from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (m + 2) for _ in range(2)]
        result = 0
        for i in range(1, n):
            dp[i % 2] = [float('-inf')] * (m + 2)
            for j in range(m):
                for d in range(-1, 2):
                    if 0 <= j + d < m and grid[j][i] > grid[j + d][i - 1]:
                        dp[i % 2][j + 1] = max(dp[i % 2][j + 1], dp[(i + 1) % 2][j + d + 1] + 1)
                result = max(result, dp[i % 2][j + 1])
        return result
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxMoves([[187,167,209,251,152,236,263,128,135],[267,249,251,285,73,204,70,207,74],[189,159,235,66,84,89,153,111,189],[120,81,210,7,2,231,92,128,218],[193,131,244,293,284,175,226,205,245]]))  # 3