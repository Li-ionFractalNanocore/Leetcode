from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest, largest = arrays[0][0], arrays[0][-1]
        result = 0
        for i in range(1, len(arrays)):
            result = max(result, abs(arrays[i][0] - largest), abs(arrays[i][-1] - smallest))
            smallest = min(smallest, arrays[i][0])
            largest = max(largest, arrays[i][-1])
        
        return result
        