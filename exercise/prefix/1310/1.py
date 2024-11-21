from typing import List
from itertools import accumulate


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = list(accumulate(arr, initial=0, func=lambda x, y: x ^ y))
        results = []
        for l, r in queries:
            results.append(prefix[r + 1] ^ prefix[l])
        return results
        