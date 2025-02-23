from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        all_nums = []
        for i in range(m):
            for j in range(n):
                all_nums.append((grid[i][j], i, j))
        all_nums.sort(reverse=True)
        result = 0
        c = 0
        for num, i, j in all_nums:
            if c >= k:
                break
            if limits[i] > 0:
                result += num
                limits[i] -= 1
                c += 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSum(grid = [[1,2],[3,4]], limits = [1,2], k = 2))