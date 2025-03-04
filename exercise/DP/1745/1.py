class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if l == 1:
                    palindrome[i][j] = True
                elif l == 2:
                    palindrome[i][j] = s[i] == s[j]
                else:
                    palindrome[i][j] = s[i] == s[j] and palindrome[i + 1][j - 1]
        dp = palindrome[0]
        for k in range(1, 3):
            for j in range(n - 1, - 1, -1):
                r = False
                for m in range(j):
                    if palindrome[0][m] and palindrome[m + 1][j]:
                        r = True
                        break
                dp[j] = r
        return dp[-1]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPartitioning(s = "abcbdd"))  # True
    print(solution.checkPartitioning(s = "bcbddxy"))  # False
                    

        