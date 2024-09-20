from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = list(map(int, str(n)))
        n = len(digits)

        @cache
        def dfs(i, existed, bound):
            if i == n:
                if existed == 0:
                    return 0
                return 1
            res = 0
            end = digits[i] + 1 if bound or i == 0 else 10
            for j in range(end):
                if existed & 1 << j:
                    continue
                next_bound = bound and j == digits[i]
                next_existed = 0 if existed == 0 and j == 0 else existed | 1 << j
                res += dfs(i + 1, next_existed, next_bound)
            return res

        return dfs(0, 0, True)

                
if __name__ == '__main__':
    solution = Solution()
    print(solution.countSpecialNumbers(135))  # 110
    print(solution.countSpecialNumbers(20))  # 19
    print(solution.countSpecialNumbers(5))  # 5