class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = min(dp[i], max(j, dp[i - j] + 1))
        return dp[n]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoEggDrop(2)) # 2
    print(solution.twoEggDrop(5)) # 3
    print(solution.twoEggDrop(100)) # 14