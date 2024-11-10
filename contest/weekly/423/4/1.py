from functools import cache

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        num_k = {1: 1}
        for i in range(2, n + 1):
            num_k[i] = num_k[i.bit_count()] + 1

        @cache
        def dfs(i, count, equal):
            if i == n:
                if count > 0 and num_k[count] <= k and not equal:
                    return 1
                else:
                    return 0
            result = 0
            if equal:
                if s[i] == '1':
                    result = dfs(i + 1, count + 1, True) + dfs(i + 1, count, False)
                else:
                    result = dfs(i + 1, count, True)
            else:
                result = dfs(i + 1, count + 1, False) + dfs(i + 1, count, False)
            return result % MOD
        
        return dfs(0, 0, True)

if __name__ == '__main__':
    solution = Solution()
    print(solution.countKReducibleNumbers("1000", 2))  # 6
    print(solution.countKReducibleNumbers("111", 1))  # 3
    print(solution.countKReducibleNumbers("1", 3))  # 0
        