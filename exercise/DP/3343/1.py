MOD = 10 ** 9 + 7
MX = 81
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD
inv_fac = [0] * MX
inv_fac[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 2, -1, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        counter = [0] * 10
        sum_ = 0
        for c in num:
            c_int = int(c)
            counter[c_int] += 1
            sum_ += c_int
        if sum_ % 2:
            return 0

        choose_n = n // 2
        choose_sum = sum_ // 2
        dp = [[0] * (choose_sum + 1) for _ in range(choose_n + 1)]
        dp[0][0] = 1
        for c in num:
            c_int = int(c)
            for i in range(choose_n, 0, -1):
                for j in range(choose_sum + 1):
                    if j + c_int <= choose_sum:
                        dp[i][j + c_int] = (dp[i][j + c_int] + dp[i-1][j]) % MOD
        result = dp[choose_n][choose_sum] * fac[choose_n] * fac[n-choose_n] % MOD
        for c in counter:
            result = result * inv_fac[c] % MOD
        return result % MOD


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBalancedPermutations("123"))
        
