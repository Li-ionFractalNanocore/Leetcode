from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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
                father[root_x] = root_y
        
        for x, y in edges:
            if root(x) == root(y):
                return [x, y]
            union(x, y)
