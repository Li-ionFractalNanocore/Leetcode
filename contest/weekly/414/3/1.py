from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        max_num = nums[0]
        n = len(nums)
        result = 0
        for i in range(1, n):
            result += max_num
            max_num = max(max_num, nums[i])
        return result