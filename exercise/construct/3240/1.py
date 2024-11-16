from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m // 2):
            for j in range(n // 2):
                c = grid[i][j] + grid[m-i-1][j] + grid[i][n-j-1] + grid[m-i-1][n-j-1]
                count += min(c, 4 - c)
        
        if m % 2 == 1 and n % 2 == 1:
            count += grid[m//2][n//2]
        
        diff = 0
        one = 0
        if m % 2 == 1:
            for i in range(n // 2):
                if grid[m//2][i] != grid[m//2][n-i-1]:
                    diff += 1
                if grid[m//2][i] == grid[m//2][n-i-1] == 1:
                    one += 2
        if n % 2 == 1:
            for i in range(m // 2):
                if grid[i][n//2] != grid[m-i-1][n//2]:
                    diff += 1
                if grid[i][n//2] == grid[m-i-1][n//2] == 1:
                    one += 2
        if diff > 0:
            return count + diff
        else:
            return count + one % 4
            

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minFlips([[0,0,0],[1,1,0],[0,1,1],[0,0,1]]))
    print(solution.minFlips([[0,1],[0,1],[0,0]]))
    print(solution.minFlips([[1,0,0],[0,1,0],[0,0,1]]))