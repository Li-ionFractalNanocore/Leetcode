from typing import List
from itertools import accumulate


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        len = sum(distance)
        prefix = list(accumulate(distance, initial=0))
        sum_ = sum(distance)
        start, destination = min(start, destination), max(start, destination)
        delta = prefix[destination] - prefix[start]
        return min(delta, sum_ - delta)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.distanceBetweenBusStops([1,2,3,4], start=0, destination=1))  # 1
    print(solution.distanceBetweenBusStops([1,2,3,4], start=0, destination=2))  # 3
    print(solution.distanceBetweenBusStops([1,2,3,4], start=0, destination=3))  # 4