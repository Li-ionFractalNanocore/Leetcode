from typing import List
from functools import cache
from math import gcd


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(i, j, k):
            if i < 0:
                if j == k:
                    return 1
                else:
                    return 0
            num = nums[i]
            return (dfs(i - 1, j, k) + dfs(i - 1, gcd(j, num), k) + dfs(i - 1, j, gcd(k, num))) % MOD

        return (dfs(len(nums) - 1, 0, 0) - 1) % MOD
        