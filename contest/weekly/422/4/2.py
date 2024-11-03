from functools import cache


# WA
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        MOD = 10 ** 9 + 7
        counter = [0] * 10
        sum_ = 0
        for c in num:
            c_int = int(c)
            counter[c_int] += 1
            sum_ += c_int
        if sum_ % 2:
            return 0

        @cache
        def dfs(digit, a, b, diff):
            if digit == 10:
                if a == b == diff == 0:
                    return 1
                else:
                    return 0
            if counter[digit] == 0:
                return dfs(digit + 1, a, b, diff)
            
            result = 0
            for i in range(min(counter[digit], a) + 1):
                for j in range(min(counter[digit] - i, b) + 1):
                    result += dfs(digit + 1, a - i, b - j, diff + (i - j) * digit)
            
            return result % MOD

        return dfs(0, n // 2 + n % 2, n // 2, 0)
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.countBalancedPermutations("123"))
    print(solution.countBalancedPermutations("53374"))
    print(solution.countBalancedPermutations("962698867371637231389"))
    print(solution.countBalancedPermutations("112"))
    print(solution.countBalancedPermutations("12345"))