from typing import List
from functools import cache


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        m, n = len(a), len(b)

        @cache
        def dfs(i, j):
            if i == m:
                return 0
            if j == n:
                return float('-inf')
            return max(dfs(i + 1, j + 1) + a[i] * b[j], dfs(i, j + 1))
        
        return dfs(0, 0)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore([-1,4,5,-2], [-5,-1,-3,-2,-4]))  # -1
    print(solution.maxScore([3,2,5,6], [2,-6,4,-5,-3,2,-7]))  # 26
