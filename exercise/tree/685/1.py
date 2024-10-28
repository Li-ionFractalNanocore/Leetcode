from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        father = [i for i in range(n + 1)]

        def root(x):
            if father[x] != x:
                father[x] = root(father[x])
            return father[x]

        def union(x, y):
            root_x = root(x)
            root_y = root(y)
            if root_x != root_y:
                father[root_y] = root_x

        conflict = -1
        cycle = -1
        parent = [i for i in range(n + 1)]
        for i, (x, y) in enumerate(edges):
            if father[y] != y:
                conflict = i
            else:
                parent[y] = x
                if root(x) == root(y):
                    cycle = i
                else:
                    union(x, y)

        if conflict < 0:
            return edges[cycle]
        else:
            conflict_edge = edges[conflict]
            if cycle < 0:
                return conflict_edge
            else:
                return [parent[conflict_edge[1]], conflict_edge[1]]

                
if __name__ == '__main__':
    solution = Solution()
    print(solution.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))  # [4, 1]