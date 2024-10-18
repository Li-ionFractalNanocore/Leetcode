from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip = 0
        res = 0
        for i in range(len(nums)):
            if (nums[i] + flip) & 1 == 0:
                res += 1
                flip = 1 - flip
        return res
        