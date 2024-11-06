from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        increase = 0
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1] + 1:
                increase += 1
            else:
                increase = 1
            if i >= k - 1:
                if increase >= k:
                    result.append(nums[i])
                else:
                    result.append(-1)
        return result
        