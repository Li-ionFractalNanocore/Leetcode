from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            factor = 0
            while num:
                result += num % 10 * factor
                num //= 10
                factor = factor * 10 + 9
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.differenceOfSum([1,15,6,3]))  # 9