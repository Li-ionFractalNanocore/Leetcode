from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = defaultdict(int)
        result = 0
        now = 0
        counter[0] = 1
        for num in nums:
            now += num
            mod = now % k
            result += counter[mod]
            counter[mod] += 1
        return result
