from functools import cache


class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        mapping = {'F': 0, 'W': 1, 'E': 2}
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, diff, now):
            if i == 0:
                if diff == 1 and (now - mapping[s[i]] + 3) % 3 == 1:
                    return 1
                if diff == -1 and (now - mapping[s[i]] + 3) % 3 == 2:
                    return 1
                if diff == 0 and (now - mapping[s[i]]) % 3 == 0:
                    return 1
                return 0
            res = 0
            if (now - mapping[s[i]] + 3) % 3 == 1:
                res += dfs(i - 1, diff - 1, (now + 1) % 3) + dfs(i - 1, diff - 1, (now + 2) % 3)
            elif (now - mapping[s[i]] + 3) % 3 == 2:
                res += dfs(i - 1, diff + 1, (now + 1) % 3) + dfs(i - 1, diff + 1, (now + 2) % 3)
            else:
                res += dfs(i - 1, diff, (now + 1) % 3) + dfs(i - 1, diff, (now + 2) % 3)
            res %= MOD
            return res

        result = 0
        for i in range(1, n + 1):
            for j in range(3):
                result = (result + dfs(n - 1, i, j)) % MOD

        return result
                

if __name__ == '__main__':
    solution = Solution()
    print(solution.countWinningSequences("F")) # 1
    print(solution.countWinningSequences("FFF")) # 3
    print(solution.countWinningSequences("FWEFW")) # 18
                
            
            
