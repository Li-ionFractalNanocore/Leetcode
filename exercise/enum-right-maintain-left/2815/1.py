from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_digit_dict = dict()
        result = -1
        for num in nums:
            max_digit = 0
            t = num
            while t:
                max_digit = max(max_digit, t % 10)
                t //= 10
            if max_digit in max_digit_dict:
                result = max(result, max_digit_dict[max_digit] + num)            
                max_digit_dict[max_digit] = max(max_digit_dict[max_digit], num)
            else:
                max_digit_dict[max_digit] = num 
        return result

