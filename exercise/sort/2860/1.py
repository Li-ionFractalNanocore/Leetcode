from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n + 1):
            if (i == n or i < nums[i]) and (i == 0 or i > nums[i-1]):
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countWays([1, 1])) # 2
    print(solution.countWays([6,0,3,3,6,7,2,7]))

