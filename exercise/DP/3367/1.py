from typing import List


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        graph = {i: {} for i in range(n)}
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        def dfs(node, parent):
            base = 0
            diff = []
            for child in graph[node]:
                if child == parent:
                    continue
                ns, s = dfs(child, node)
                base += ns
                d = s + graph[node][child] - ns
                if d > 0:
                    diff.append(d)
            diff.sort(reverse=True)
            return base + sum(diff[:k]), base + sum(diff[:k - 1])
        
        return dfs(0, -1)[0]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximizeSumOfWeights([[0, 1, 4], [0, 2, 2], [2, 3, 12], [2, 4, 6]], 2))
            
            