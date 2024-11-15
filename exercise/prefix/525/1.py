from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = {0: -1}
        count_diff = 0

        result = 0
        for i, num in enumerate(nums):
            if num == 0:
                count_diff -= 1
            else:
                count_diff += 1
            if count_diff in counter:
                result = max(result, i - counter[count_diff])
            else:
                counter[count_diff] = i
        return result
        