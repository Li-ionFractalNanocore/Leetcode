from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev_diff(n):
            return int(str(n)[::-1]) - n

        counter = defaultdict(int)
        result = 0
        MOD = 10**9 + 7
        for num in nums:
            result += counter[rev_diff(num)] % MOD
            counter[rev_diff(num)] += 1
        return result % MOD