from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
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
        
        dis1 = [0] * 2
        is_odd = [False] * n
        dis2 = [0] * 2
        visited = set()

        def dfs(graph, dis, u, now, d, record=False):
            dis[d % 2] += 1
            if record:
                is_odd[now] = d % 2 == 1
            for v in graph[now]:
                if v in visited:
                    continue
                visited.add(v)
                dfs(graph, dis, u, v, d + 1, record)
        
        visited.add(0)
        dfs(graph1, dis1, 0, 0, 0, True)
        visited.clear()
        visited.add(0)
        dfs(graph2, dis2, 0, 0, 0)

        max_ext = max(dis2)
        results = []
        for i in range(n):
            if is_odd[i]:
                result = dis1[1] + max_ext
            else:
                result = dis1[0] + max_ext
            results.append(result)

        return results

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]])) #[8, 7, 7, 8, 8]
    print(solution.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]])) #[3, 6, 6, 6, 6]