from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = dp_min[0] = grid[0][0]
        for i in range(1, n):
            dp_max[i] = dp_min[i] = dp_max[i-1] * grid[0][i]
        for i in range(1, m):
            new_dp_max = [0] * n
            new_dp_min = [0] * n
            new_dp_max[0] = max(dp_max[0] * grid[i][0], dp_min[0] * grid[i][0])
            new_dp_min[0] = min(dp_max[0] * grid[i][0], dp_min[0] * grid[i][0])
            for j in range(1, n):
                new_dp_max[j] = max(dp_max[j] * grid[i][j], dp_min[j] * grid[i][j], new_dp_max[j-1] * grid[i][j], new_dp_min[j-1] * grid[i][j])
                new_dp_min[j] = min(dp_max[j] * grid[i][j], dp_min[j] * grid[i][j], new_dp_max[j-1] * grid[i][j], new_dp_min[j-1] * grid[i][j])
            dp_max = new_dp_max
            dp_min = new_dp_min
        return dp_max[-1] % MOD if dp_max[-1] >= 0 else -1

        