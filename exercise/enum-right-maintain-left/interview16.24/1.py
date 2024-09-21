from typing import List
from collections import defaultdict


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        counter = defaultdict(int)
        for num in nums:
            if counter[target - num] > 0:
                result.append([target - num, num])
                counter[target - num] -= 1
            else:
                counter[num] += 1
        return result