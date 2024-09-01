from typing import List
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        result = 0
        for num in nums:
            result += counter[num]
            counter[num] += 1
        return result