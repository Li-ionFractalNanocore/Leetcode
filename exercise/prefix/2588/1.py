from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        now = 0
        counter[0] = 1
        result = 0
        for num in nums:
            now ^= num
            result += counter[now]
            counter[now] += 1
        return result
        