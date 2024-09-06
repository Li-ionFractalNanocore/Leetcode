from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        result = 0
        for price in prices:
            delta = price - min_value
            result = max(result, delta)
            min_value = min(min_value, price)
        return result