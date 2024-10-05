from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, min(time) * totalTrips
        while l < r:
            m = (l + r) // 2
            trips = sum(m // t for t in time)
            if trips < totalTrips:
                l = m + 1
            else:
                r = m
        return l