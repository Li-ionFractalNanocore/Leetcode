from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        largest = {}
        result = -1

        def digit(num):
            result = 0
            while num > 0:
                result += num % 10
                num //= 10
            return result
        
        for num in nums:
            digit_sum = digit(num)
            if digit_sum in largest:
                result = max(result, num + largest[digit_sum])
                largest[digit_sum] = max(largest[digit_sum], num)
            else:
                largest[digit_sum] = num
        return result
            
        