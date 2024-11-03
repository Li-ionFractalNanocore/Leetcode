from functools import cache


# TLE
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
        remained = 0
        for i, num in enumerate(counter):
            remained += num << (i * 7)

        @cache
        def dfs(i, j, remained):
            if i == -1:
                if j == 0:
                    return 1
                else:
                    return 0
            if abs(j) > (i + 1) * 9:
                return 0
            
            result = 0
            for k in range(10):
                count = remained >> (k * 7) & 127
                if count:
                    if i & 1:
                        result += dfs(i - 1, j + k, remained & ~(127 << (k * 7)) | (count - 1) << (k * 7))
                    else:
                        result += dfs(i - 1, j - k, remained & ~(127 << (k * 7)) | (count - 1) << (k * 7))
                
            return result % MOD

        return dfs(n-1, 0, remained)
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.countBalancedPermutations("962698867371637231389"))
    print(solution.countBalancedPermutations("53374"))
    print(solution.countBalancedPermutations("123"))
    print(solution.countBalancedPermutations("112"))
    print(solution.countBalancedPermutations("12345"))