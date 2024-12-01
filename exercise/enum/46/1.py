from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        remain = [True] * n
        path = [0] * n

        def dfs(i):
            if i == len(nums):
                results.append(path.copy())
                return
            for j, num in enumerate(nums):
                if remain[j]:
                    remain[j] = False
                    path[i] = num
                    dfs(i + 1)
                    remain[j] = True
            
        dfs(0)
        return results

                
        