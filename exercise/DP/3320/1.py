from functools import cache


class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        mapping = {'F': 0, 'W': 1, 'E': 2}
        MOD = 10 ** 9 + 7
        s_int = [mapping[c] for c in s]

        @cache
        def dfs(i, diff, pre):
            if diff + i < 0:
                return 0
            if diff - i - 1 > 0:
                return pow(2, i + 1, MOD)
            result = 0
            for j in range(3):
                if j == pre:
                    continue
                score = (j - s_int[i] + 3) % 3
                if score == 2:
                    score = -1
                result += dfs(i - 1, diff + score, j)
            return result % MOD

        return dfs(n - 1, 0, -1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countWinningSequences("FFF")) # 3
    print(solution.countWinningSequences("FWEFW")) # 18