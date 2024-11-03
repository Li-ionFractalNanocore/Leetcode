from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        way = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [(0, 0, 0)]
        visited = set([(0, 0)])
        while queue:
            t, x, y = heapq.heappop(queue)
            if x == m - 1 and y == n - 1:
                return t
            for dx, dy in way:
                nx, ny = x + dx, y + dy
                delta = 2 - (nx + ny) % 2
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    nt = max(t, moveTime[nx][ny]) + delta
                    heapq.heappush(queue, (nt, nx, ny))


if __name__ == '__main__':
    solution = Solution()
    print(solution.minTimeToReach([[15,58],[67,4]]))
    print(solution.minTimeToReach([[0,4], [4,4]]))
    print(solution.minTimeToReach([[0,1], [1,2]]))
    print(solution.minTimeToReach([[0,0,0], [0,0,0]]))
    print(solution.minTimeToReach([[0,0,0,0], [0,0,0,0]]))