from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        graph1 = [[] for _ in range(n)]
        graph2 = [[] for _ in range(m)]
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
        dis1 = [[0] * (k + 1) for _ in range(n)]
        dis2 = [[0] * (k + 1) for _ in range(m)]
        visited = set()

        def dfs(graph, dis, u, now, d):
            dis[u][d] += 1
            if d == k:
                return
            for v in graph[now]:
                if v in visited:
                    continue
                visited.add(v)
                dfs(graph, dis, u, v, d + 1)
        
        for i in range(n):
            visited.add(i)
            dfs(graph1, dis1, i, i, 0)
            visited.clear()
            for j in range(1, k + 1):
                dis1[i][j] += dis1[i][j - 1]
        
        for i in range(m):
            visited.add(i)
            dfs(graph2, dis2, i, i, 0)
            visited.clear()
            for j in range(1, k + 1):
                dis2[i][j] += dis2[i][j - 1]

        max_ext = 0
        if k > 0:
            for i in range(m):
                max_ext = max(max_ext, dis2[i][k - 1])
        result = [1] * n
        for i in range(n):
            result[i] = max_ext + dis1[i][k]

        return result
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2)) #[9, 7, 9, 8, 8]
    print(solution.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1)) #[6, 3, 3, 3, 3]