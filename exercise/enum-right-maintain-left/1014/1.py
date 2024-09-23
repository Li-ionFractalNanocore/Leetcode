from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_val = values[0] - 1
        result = float('-inf')

        for i in range(1, n):
            result = max(result, max_val + values[i])
            max_val = max(max_val, values[i]) - 1
        
        return result
            
