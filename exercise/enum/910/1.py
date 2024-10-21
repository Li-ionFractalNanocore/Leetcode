from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = float('inf')
        for i in range(n):
            max_num = max(nums[i] + k, nums[-1] - k)
            if i < n - 1:
                min_num = min(nums[0] + k, nums[i+1] - k)
            else:
                min_num = nums[0] + k
            result = min(result, max_num - min_num)
        return result
            