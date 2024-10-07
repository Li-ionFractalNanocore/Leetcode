from typing import List
from heapq import heappop, heappush


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        n = len(nums)
        hp = 1
        hp_heap = []
        counter = 0
        for i in range(n):
            if nums[i] < 0:
                heappush(hp_heap, nums[i])
            hp += nums[i]
            while hp <= 0:
                hp -= heappop(hp_heap)
                counter += 1
        return counter