class Solution:
    def knightDialer(self, n: int) -> int:
        next_pos = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        dp = [1] * 10
        for i in range(1, n):
            new_dp = [0] * 10
            for j in range(10):
                for k in next_pos[j]:
                    new_dp[j] += dp[k]
                    new_dp[j] %= 10**9 + 7
            dp = new_dp
        return sum(dp) % (10**9 + 7)
        