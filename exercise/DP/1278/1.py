from functools import cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        def check(i, j):
            result = 0
            while i < j:
                if s[i] != s[j]:
                    result += 1
                i += 1
                j -= 1
            return result

        @cache
        def dfs(i, remain):
            if i < remain:
                return 0
            if remain == 0:
                return check(0, i)
            result = float('inf')
            for j in range(remain - 1, i):
                result = min(result, dfs(j, remain - 1) + check(j + 1, i))
            return result
        
        return dfs(len(s) - 1, k - 1)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.palindromePartition(s = "aea", k = 2))  # 1
    print(solution.palindromePartition(s = "aabbc", k = 3))  # 0
    print(solution.palindromePartition(s = "abc", k = 2))  # 1
    print(solution.palindromePartition(s = "leetcode", k = 8))  # 0


        