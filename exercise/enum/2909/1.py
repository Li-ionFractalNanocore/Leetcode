from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_min = [float('inf')] * len(nums)
        suffix_min = nums[-1]
        result = float('inf')
        for i in range(n):
            prefix_min[i] = min(prefix_min[i - 1], nums[i])
        for i in range(n - 2, 0, -1):
            if prefix_min[i - 1] < nums[i] and suffix_min < nums[i]:
                result = min(result, prefix_min[i - 1] + suffix_min + nums[i])
            suffix_min = min(suffix_min, nums[i])
        return result if result != float('inf') else -1
            