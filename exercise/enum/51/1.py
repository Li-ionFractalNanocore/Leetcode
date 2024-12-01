from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        path = [0] * n
        remain = [True] * n
        add = [True] * (2 * n - 1)
        sub = [True] * (2 * n - 1)

        def dfs(i):
            if i == n:
                result = []
                for j in range(n):
                    row = ['.'] * n
                    row[path[j]] = 'Q'
                    result.append(''.join(row))
                results.append(result)
            for num in range(n):
                if remain[num] and add[i + num] and sub[i - num]:
                    remain[num] = add[i + num] = sub[i - num] = False
                    path[i] = num
                    dfs(i + 1)
                    remain[num] = add[i + num] = sub[i - num] = True
            
        dfs(0)
        return results
            
            
        