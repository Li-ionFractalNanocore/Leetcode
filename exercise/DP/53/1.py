from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        f = nums[0]
        for num in nums[1:]:
            f = max(f + num, num)
            result = max(result, f)
        return result