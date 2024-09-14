from typing import List
from collections import deque
from functools import cache


WAYS = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        n = len(positions)
        m = 50

        def bfs(x, y):
            dis = [[float('inf')] * m for _ in range(m)]
            queue = deque([(x, y)])
            dis[x][y] = 0
            while queue:
                x, y = queue.popleft()
                for way in WAYS:
                    nx, ny = x + way[0], y + way[1]
                    if 0 <= nx < m and 0 <= ny < m and dis[nx][ny] == float('inf'):
                        dis[nx][ny] = dis[x][y] + 1
                        queue.append((nx, ny))
            return dis

        distances = [dis for dis in map(lambda pos: bfs(*pos), positions)]
        full = (1 << n) - 1
        positions.append([kx, ky])

        @cache
        def alice(last, visited):
            if visited == full:
                return 0
            x, y = positions[last]
            res = 0
            for i, dis in enumerate(distances):
                if visited & (1 << i) == 0:
                    res = max(res, bob(i, visited | (1 << i)) + dis[x][y])
            return res

        @cache
        def bob(last, visited):
            if visited == full:
                return 0
            x, y = positions[last]
            res = float('inf')
            for i, dis in enumerate(distances):
                if visited & (1 << i) == 0:
                    res = min(res, alice(i, visited | (1 << i)) + dis[x][y])
            return res
        
        return alice(n, 0)
            

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxMoves(0, 2, [[1, 1], [2, 2], [3, 3]]))  # 8
    print(solution.maxMoves(1, 1, [[0, 0]]))  # 4