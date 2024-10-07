from typing import List
from heapq import heappop, heappush


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        
        now = 0
        fuel_now = startFuel
        fuels = []
        result = 0
        for pos, fuel in stations:
            fuel_now -= pos - now
            while fuels and fuel_now < 0:
                fuel_now += -heappop(fuels)
                result += 1
            if fuel_now < 0:
                return -1
            heappush(fuels, -fuel)
            now = pos
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))  # 2

