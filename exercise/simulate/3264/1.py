from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        q = []
        for i, num in enumerate(nums):
            heapq.heappush(q, (num, i))
        for _ in range(k):
            num, i = heapq.heappop(q)
            num *= multiplier
            heapq.heappush(q, (num, i))
        results = [0] * len(nums)
        for num, i in q:
            results[i] = num
        return results
