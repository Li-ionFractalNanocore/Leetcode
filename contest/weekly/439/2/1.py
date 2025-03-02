from functools import cache

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:

        def check_same(a, b, k):
            ord_a = ord(a)
            ord_b = ord(b)
            ord_a, ord_b = min(ord_a, ord_b), max(ord_a, ord_b)
            if ord_b - ord_a <= k or ord_a + 26 - ord_b <= k:
                return min(ord_b - ord_a, ord_a + 26 - ord_b)
            else:
                return -1

        @cache
        def dfs(start, end, k):
            if start == end:
                return 1
            if start == end - 1:
                if check_same(s[start], s[end], k) >= 0:
                    return 2
                else:
                    return 1
            use_k = check_same(s[start], s[end], k)
            result = max(dfs(start + 1, end, k), dfs(start, end - 1, k))
            if use_k < 0:
                return result
            else:
                return max(2 + dfs(start + 1, end - 1, k - use_k), result)

        return dfs(0, len(s) - 1, k)
            

if __name__ == '__main__':
    solution = Solution()

    print(solution.longestPalindromicSubsequence(s = "nyjejp", k = 8))  # 5
    print(solution.longestPalindromicSubsequence(s = "wehzr", k = 3))  # 3
    print(solution.longestPalindromicSubsequence(s = "abced", k = 2))  # 3