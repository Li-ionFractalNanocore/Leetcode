from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = defaultdict(int)
        for i, num in enumerate(nums):
            if i > k:
                counter[nums[i-k-1]] -= 1
            if counter[num] > 0:
                return True
            counter[num] += 1
        return False
            
