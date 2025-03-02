class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(n - 1):
            is_palindrome[i][i + 1] = s[i] == s[i + 1]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
        
        dp = [float('inf')] * n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
                continue
            for j in range(1, i + 1):
                if is_palindrome[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
        return dp[-1]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut(s = "aab"))  # 1
    print(solution.minCut(s = "a"))  # 0
    print(solution.minCut(s = "ab"))  # 1