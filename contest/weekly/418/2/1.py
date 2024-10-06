from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = [[] for _ in range(n)]
        for invocation in invocations:
            edges[invocation[0]].append(invocation[1])

        doubt = set()

        def dfs_doubt(node):
            for next_node in edges[node]:
                if next_node not in doubt:
                    doubt.add(next_node)
                    dfs_doubt(next_node)

        doubt.add(k)
        dfs_doubt(k)

        for i in range(n):
            if i in doubt:
                continue
            for next_node in edges[i]:
                if next_node in doubt:
                    return list(range(n))

        return list(set(range(n)) - doubt)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.remainingMethods(n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]))  # [0, 1, 2, 3]
    print(solution.remainingMethods(n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]))  # [3, 4]
    print(solution.remainingMethods(n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]))  # []
            
            