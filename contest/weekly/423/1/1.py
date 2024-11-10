from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        incresed = [False] * n
        increasing_len = 1
        if k == 1:
            incresed[0] = True
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing_len += 1
            else:
                increasing_len = 1
            if increasing_len >= k:
                incresed[i] = True
                if i >= k and incresed[i - k]:
                    return True
        return False

        