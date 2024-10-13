class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        mapping = {'F': 0, 'W': 1, 'E': 2}
        MOD = 10 ** 9 + 7

        dp = [[0 for _ in range(3)] for _ in range(2*n+1)]

        for now in range(3):
            if (now - mapping[s[0]] + 3) % 3 == 1:
                dp[n+1][now] = 1
            elif (now - mapping[s[0]] + 3) % 3 == 2:
                dp[n-1][now] = 1
            elif (now - mapping[s[0]]) % 3 == 0:
                dp[n][now] = 1

        for i in range(1, n):
            last_r = [0, 0, 0]
            for diff in range(n, -n-1, -1):
                now_r = [0, 0, 0]
                for now in range(3):
                    if (now - mapping[s[i]] + 3) % 3 == 1 and diff > -n:
                        now_r[now] = (dp[diff+n-1][(now+1)%3] + dp[diff+n-1][(now+2)%3]) % MOD
                    elif (now - mapping[s[i]] + 3) % 3 == 2 and diff < n:
                        now_r[now] = (dp[diff+n+1][(now+1)%3] + dp[diff+n+1][(now+2)%3]) % MOD
                    else:
                        now_r[now] = (dp[diff+n][(now+1)%3] + dp[diff+n][(now+2)%3]) % MOD
                if diff < n:
                    dp[diff+n+1] = last_r
                last_r = now_r

        result = 0
        for i in range(1, n + 1):
            for j in range(3):
                result = (result + dp[i+n][j]) % MOD

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countWinningSequences("FFF")) # 3
    print(solution.countWinningSequences("FWEFW")) # 18