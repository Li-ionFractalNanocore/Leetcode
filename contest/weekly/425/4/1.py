from typing import List


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        result = 0
        now = 0
        degree = [[] for _ in range(n)]
        edges.sort(key=lambda x: -x[2])

        def remove_last(u):
            t, d = degree[u].pop()
            degree[t].remove((u, d))
            return d

        for u, v, w in edges:
            if len(degree[u]) < k and len(degree[v]) < k:
                degree[u].append((v, w))
                degree[v].append((u, w))
                now += w
            else:
                if len(degree[u]) == k:
                    d = remove_last(u)
                    now -= d
                if len(degree[v]) == k:
                    d = remove_last(v)
                    now -= d
                degree[u].append((v, w))
                degree[v].append((u, w))
                now += w
            result = max(result, now)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximizeSumOfWeights([[0,1,4],[0,2,2],[2,3,12],[2,4,6]], 2))  # 22
        