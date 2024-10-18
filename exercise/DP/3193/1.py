from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        requirements_map = {k: v for k, v in requirements}
        max_m = max(requirements_map.values())
        if 0 in requirements_map and requirements_map[0] != 0:
            return 0
        dp = [0] * (max_m + 1)
        dp[0] = 1
        for i in range(1, n):
            for j in range(1, max_m + 1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD
            for j in range(max_m, -1, -1):
                if i in requirements_map and j != requirements_map[i]:
                    dp[j] = 0
                    continue
                if j > i:
                    dp[j] = (dp[j] - dp[j - i - 1]) % MOD
        return dp[requirements_map[n - 1]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfPermutations(3, [[2, 2], [0, 0]])) # 2
    print(solution.numberOfPermutations(3, [[2, 2], [1, 1], [0, 0]])) # 1