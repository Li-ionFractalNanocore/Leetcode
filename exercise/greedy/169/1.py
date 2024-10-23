from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        now, cnt = nums[0], 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] == now:
                cnt += 1
            elif cnt == 0:
                now, cnt = nums[i], 1
            else:
                cnt -= 1
        return now