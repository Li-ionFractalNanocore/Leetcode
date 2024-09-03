from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        max_, min_ = nums[0], nums[0]
        for i in range(1, n):
            new_max_ = max(max_, max_ * nums[i], min_ * nums[i], nums[i])
            min_ = min(min_, max_ * nums[i], min_ * nums[i], nums[i])
            max_ = new_max_
        return max_
