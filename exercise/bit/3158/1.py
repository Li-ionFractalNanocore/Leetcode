from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        num_set = set(nums)
        for num in num_set:
            res ^= num
        return res