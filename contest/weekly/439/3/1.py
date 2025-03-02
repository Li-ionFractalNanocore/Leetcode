from typing import List
from functools import cache


class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:

        @cache
        def dfs(end, choose_n):
            if end == 0:
                if choose_n == 1:
                    return nums[0]
                else:
                    return -float('inf')
            if choose_n == 0:
                return -float('inf')
            result = dfs(end - 1, choose_n) + nums[end]
            if choose_n == 1:
                result = max(result, nums[end])
            for last in range(end):
                result = max(result, dfs(last, choose_n - 1) + nums[end])
            return result

        result = -float('inf')
        for i in range(len(nums)):
            result = max(result, dfs(i, k))
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSum(nums = [1,2,-1,3,3,4], k = 2, m = 2))  # 13
    print(solution.maxSum(nums = [-10, 3, -1, -2], k = 4, m = 1))  # -10