from typing import List
from itertools import accumulate


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = list(accumulate(nums, initial=0))
        results = []
        for i, num in enumerate(nums):
            left = num * i - prefix[i]
            right = prefix[-1] - prefix[i + 1] - num * (n - i - 1)
            results.append(left + right)
        return results
        