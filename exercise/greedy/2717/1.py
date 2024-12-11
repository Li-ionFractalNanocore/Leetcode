from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        one_axis = -1
        n_axis = -1
        for i in range(n):
            if nums[i] == 1:
                one_axis = i
            if nums[i] == n:
                n_axis = i
        if one_axis > n_axis:
            return one_axis + (n - n_axis - 1) - 1
        return one_axis + (n - n_axis - 1)
        