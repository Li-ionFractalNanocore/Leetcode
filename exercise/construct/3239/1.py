from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n-j-1]:
                    row += 1
        col = 0
        for i in range(n):
            for j in range(m // 2):
                if grid[j][i] != grid[m-j-1][i]:
                    col += 1
        return min(row, col)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minFlips([[1,0,0],[0,0,0],[0,0,1]]))
        