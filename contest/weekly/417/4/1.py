import math
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(index):
            now = math.ceil(math.log2(index + 1)) - 1
            if now == -1:
                return 0
            if operations[now] == 1:
                return dfs(index - (1 << now)) + 1
            if operations[now] == 0:
                return dfs(index - (1 << now))
            
        return chr(ord('a') + dfs(k - 1) % 26)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.kthCharacter(16, [1, 1, 1, 1])) # b
    print(solution.kthCharacter(5, [0, 0, 0])) # a
    print(solution.kthCharacter(10, [0, 1, 0, 1])) # b