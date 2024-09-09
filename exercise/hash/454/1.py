from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = defaultdict(int)
        for a in nums1:
            for b in nums2:
                counter[a + b] += 1
        result = 0
        for c in nums3:
            for d in nums4:
                result += counter[-c - d]
        return result