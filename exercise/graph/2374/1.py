from typing import List
from collections import defaultdict


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        count = defaultdict(int)
        result, no = 0, -1
        for i, edge in enumerate(edges):
            count[edge] += i
            if result < count[edge] or (result == count[edge] and no > edge):
                result = count[edge]
                no = edge
        return no
            