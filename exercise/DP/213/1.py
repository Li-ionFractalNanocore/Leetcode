from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        first, second = nums[0], nums[0]
        for i in range(2, n - 1):
            first, second = second, max(first + nums[i], second)
        result = max(first, second)
        first, second = 0, nums[1]
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
        return max(result, second)


solution = Solution()
print(solution.rob([2, 3, 2]))  # 3
print(solution.rob([1, 2, 3, 1]))  # 4
print(solution.rob([1, 2, 3]))  # 3  
print(solution.rob([4,1,2,7,5,3,1]))  # 14

        