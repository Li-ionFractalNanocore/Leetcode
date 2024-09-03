from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float('-inf')
        sum_ = 0
        for i, num in enumerate(nums):
            sum_ += num
            if i < k - 1:
                continue
            result = max(result, sum_ / k)
            sum_ -= nums[i - k + 1]
        return result

