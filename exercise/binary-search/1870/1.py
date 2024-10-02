import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed):
            return sum(math.ceil(d / speed) for d in dist[:-1]) + dist[-1] / speed <= hour
        l, r = 1, 10**7
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        if check(l):
            return l
        else:
            return -1

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minSpeedOnTime([1, 3, 2], 1.9))
    print(solution.minSpeedOnTime([1, 3, 2], 2.7))
    print(solution.minSpeedOnTime([1, 3, 2], 6))