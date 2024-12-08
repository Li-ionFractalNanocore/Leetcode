from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [0] * n
        for i in range(n):
            results[i] = nums[(i + nums[i]) % n]
        return results