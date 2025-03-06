from typing import List
from itertools import accumulate
from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        accum = list(accumulate(nums, initial=0, func=lambda x, y: x ^ y))
        counter = defaultdict(int)

        result = 0
        for i in range(len(accum)):
            result += counter[accum[i]]
            counter[accum[i]] += 1
        return result