from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        now = 0
        max_next = 0
        jump = 0
        for i in range(n - 1):
            if i == now:
                now = max(max_next, i + nums[i])
                jump += 1
            else:
                max_next = max(max_next, i + nums[i])
        return jump