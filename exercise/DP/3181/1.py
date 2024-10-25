from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        f = 1
        for reward in sorted(set(rewardValues)):
            f |= (f & ((1 << reward) - 1)) << reward
        return f.bit_length() - 1
        