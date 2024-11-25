from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        dis = [float('inf')] * (n + 1)
        dis[k] = 0
        next_nodes = [(0, k)]
        visited = set()

        while next_nodes:
            d, u = heapq.heappop(next_nodes)
            if u in visited:
                continue
            for v, w in graph[u]:
                if v not in visited and d + w < dis[v]:
                    dis[v] = d + w
                    heapq.heappush(next_nodes, (dis[v], v))
        result = max(dis[1:])
        return -1 if result == float('inf') else result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
            