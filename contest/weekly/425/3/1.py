from typing import List
from functools import cache

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        
        @cache
        def dfs(idx, op1_remain, op2_remain):
            if idx == len(nums):
                return 0
            if op1_remain == 0 and op2_remain == 0:
                return sum(nums[idx:])
            result = dfs(idx + 1, op1_remain, op2_remain) + nums[idx]
            if op1_remain > 0:
                result = min(result, dfs(idx + 1, op1_remain - 1, op2_remain) + (nums[idx] + 1) // 2)
            if op2_remain > 0 and nums[idx] >= k:
                result = min(result, dfs(idx + 1, op1_remain, op2_remain - 1) + nums[idx] - k)
            if op1_remain > 0 and op2_remain > 0 and nums[idx] >= k:
                result = min(result, dfs(idx + 1, op1_remain - 1, op2_remain - 1) + (nums[idx] - k + 1) // 2)
                if (nums[idx] + 1) // 2 >= k:
                    result = min(result, dfs(idx + 1, op1_remain - 1, op2_remain - 1) + (nums[idx] + 1) // 2 - k)
            return result
        
        return dfs(0, op1, op2)
                
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minArraySum([2, 5, 3], 3, 3, 1))  # 4
    print(solution.minArraySum([2, 4, 3], 3, 2, 1))  # 3
    print(solution.minArraySum([2, 8, 3, 19, 3], 3, 1, 1))  # 23