class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[i for i in range(n + 1)] for j in range(2)]

        for i in range(1, k):
            no = i % 2
            dp[no][0] = 0
            dp[no][1] = 1
            for j in range(2, n + 1):
                l, r = 1, j - 1
                while l < r:
                    m = (l + r) // 2
                    if dp[1-no][m - 1] < dp[no][j - m]:
                        l = m + 1
                    else:
                        r = m
                dp[no][j] = max(dp[1-no][l - 1], dp[no][j - l]) + 1
        return dp[1-k%2][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.superEggDrop(3, 14))  # 4
    print(solution.superEggDrop(1, 2))  # 2
    print(solution.superEggDrop(2, 6))  # 3