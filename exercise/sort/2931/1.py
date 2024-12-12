from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        indices = [n - 1] * m
        results = 0
        for i in range(m * n):
            min_index = 0
            min_value = float('inf')
            for j in range(m):
                if indices[j] >= 0 and values[j][indices[j]] < min_value:
                    min_index = j
                    min_value = values[j][indices[j]]
            results += min_value * (i + 1)
            indices[min_index] -= 1
        return results
        