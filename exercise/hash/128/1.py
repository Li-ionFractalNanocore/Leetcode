from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in nums:
                current = 1
                while num + 1 in nums:
                    current += 1
                    num += 1
                result = max(result, current)
        return result
        