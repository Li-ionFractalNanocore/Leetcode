from typing import List
from itertools import accumulate
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = accumulate(nums, initial=0)
        prefix_sum_count = defaultdict(int)
        result = 0
        for i, s in enumerate(prefix_sum):
            result += prefix_sum_count[s - k]
            prefix_sum_count[s] += 1
        return result

        