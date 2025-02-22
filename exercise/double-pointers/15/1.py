from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                while left < right and (nums[left] + nums[right] < target or left > i + 1 and nums[left] == nums[left-1]):
                    left += 1
                while left < right and (nums[left] + nums[right] > target or right < n - 1 and nums[right] == nums[right+1]):
                    right -= 1
        return result
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))