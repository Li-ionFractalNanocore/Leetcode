from typing import List

class Node:
    def __init__(self):
        self.children = {}


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = Node()
        for word in words:
            now = root
            for i in range(len(word)):
                if word[i] not in now.children:
                    now.children[word[i]] = Node()
                now = now.children[word[i]]

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for start in range(n):
            if dp[start] == float('inf'):
                break
            now = root
            for end in range(start, n):
                if target[end] not in now.children:
                    break
                dp[end+1] = min(dp[end+1], dp[start] + 1)
                now = now.children[target[end]]
        if dp[n] == float('inf'):
            return -1
        return dp[n]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minValidStrings(["abc","aaaaa","bcdef"], target="aabcdabc"))  # 3
    print(solution.minValidStrings(["abababab","ab"], target="ababaababa"))  # 2
    print(solution.minValidStrings(["abcdef"], target="xyz"))  # -1