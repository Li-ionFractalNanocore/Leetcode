
class Solution:
    def totalNQueens(self, n: int) -> int:
        results = 0
        path = [0] * n
        remain = [True] * n
        add = [True] * (2 * n - 1)
        sub = [True] * (2 * n - 1)

        def dfs(i):
            nonlocal results
            if i == n:
                results += 1
            for num in range(n):
                if remain[num] and add[i + num] and sub[i - num]:
                    remain[num] = add[i + num] = sub[i - num] = False
                    path[i] = num
                    dfs(i + 1)
                    remain[num] = add[i + num] = sub[i - num] = True
            
        dfs(0)
        return results