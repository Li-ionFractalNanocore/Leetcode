from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)

        if source == target:
            return 0
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        queue = deque([source])
        dis = {source: 0}

        while queue:
            stop = queue.popleft()
            dis_stop = dis[stop]
            for bus in stop_to_buses[stop]:
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return dis_stop + 1
                    if next_stop not in dis:
                        dis[next_stop] = dis_stop + 1
                        queue.append(next_stop)
        return -1

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)) # 2