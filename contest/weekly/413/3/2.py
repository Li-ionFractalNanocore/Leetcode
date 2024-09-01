from typing import List
from collections import defaultdict


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * (1 << m)
        positions = defaultdict(set)
        for i in range(m):
            for j in range(n):
                positions[grid[i][j]].add(i)
        result = 0
        for k, v in positions.items():
            new_dp = dp.copy()
            for x in v:
                for i in range(1 << m):
                    if (i & (1 << x)) == 0:
                        new_dp[i | (1 << x)] = max(new_dp[i | (1 << x)], dp[i] + k)
                        result = max(result, new_dp[i | (1 << x)])
            dp = new_dp
        return result


        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore([[8,11,3],[17,7,3],[13,20,3],[3,17,20]]))  # 61
    print(solution.maxScore([[i * 10 + j for j in range(1, 11)] for i in range(10)]))  # 550
    print(solution.maxScore([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 18
    print(solution.maxScore([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # 1
    print(solution.maxScore([[1, 2, 3], [4, 3, 2], [1, 1, 1]]))  # 8
    print(solution.maxScore([[8, 7, 6], [8, 3, 2]]))  # 15