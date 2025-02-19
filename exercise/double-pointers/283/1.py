from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = -1  # first zero
        for i in range(n):
            if nums[i] == 0:
                if left == -1:
                    left = i
            else:
                if left != -1:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
        
        