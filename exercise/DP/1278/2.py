
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        check = [[0] * len(s) for _ in range(len(s))]
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                check[i][j] = check[i + 1][j - 1] + (s[i] != s[j])

        dp = [[float('inf')] * k for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][0] = check[0][i]
        for i in range(1, k):
            for j in range(i, len(s)):
                for d in range(i - 1, j):
                    dp[j][i] = min(dp[j][i], dp[d][i - 1] + check[d + 1][j])
        return dp[-1][-1]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.palindromePartition(s = "tcymekt", k = 4))  # 2
    print(solution.palindromePartition(s = "aabbc", k = 3))  # 0
    print(solution.palindromePartition(s = "abc", k = 2))  # 1
    print(solution.palindromePartition(s = "leetcode", k = 8))  # 0

