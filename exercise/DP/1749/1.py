from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        num_min, num_max = 0, 0
        result = 0
        for num in nums:
            num_min = min(num + num_min, 0)
            num_max = max(num + num_max, 0)
            result = max(result, abs(num_min), abs(num_max))
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxAbsoluteSum([1, -3, 2, 3, -4]))  # 5
    print(solution.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))  # 8