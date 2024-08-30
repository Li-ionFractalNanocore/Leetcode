from typing import List
from collections import defaultdict


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        digits_n = len(str(nums[0]))
        digits_counter = [defaultdict(int) for _ in range(digits_n)]
        digits_count = [0] * digits_n

        result = 0
        for num in nums:
            i = 0
            while num:
                digit = num % 10
                num //= 10
                result += digits_count[i] - digits_counter[i][digit]
                digits_count[i] += 1
                digits_counter[i][digit] += 1
                i += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumDigitDifferences([13, 23, 12]))  # 4
    print(solution.sumDigitDifferences([10, 10, 10, 10]))  # 0
