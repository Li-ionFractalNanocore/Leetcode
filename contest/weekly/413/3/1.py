from typing import List
from collections import defaultdict


class Solution:
    # TLE
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        begin_state = 0
        dp = defaultdict(set)
        dp[0].add(begin_state)
        for i in range(m):
            new_items = defaultdict(set)
            for j in range(n):
                for k, v in dp.items():
                    for state in v:
                        if state & (1 << grid[i][j]) == 0:
                            new_state = state ^ (1 << grid[i][j])
                            new_value = k + grid[i][j]
                            if new_value in dp:
                                dp[new_value].add(new_state)
                            else:
                                new_items[new_value].add(new_state)
            dp.update(new_items)
        return max(dp.keys())

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore([[i * 10 + j for j in range(1, 11)] for i in range(10)]))  # 550
    print(solution.maxScore([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 18
    print(solution.maxScore([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # 1
    print(solution.maxScore([[1, 2, 3], [4, 3, 2], [1, 1, 1]]))  # 8
    print(solution.maxScore([[8, 7, 6], [8, 3, 2]]))  # 15