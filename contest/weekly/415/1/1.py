from typing import List
from collections import defaultdict


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        result = []
        for num in nums:
            counter[num] += 1
            if counter[num] == 2:
                result.append(num)
        return result