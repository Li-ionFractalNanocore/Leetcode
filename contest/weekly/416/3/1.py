from collections import defaultdict


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        res = 0
        r = 0
        window_counter = defaultdict(int)
        all_success = 0
        prefix_counter = defaultdict(int)

        for c in word2:
            prefix_counter[c] += 1
        all_prefix = len(prefix_counter)

        for l in range(m):
            while r < m and all_success < all_prefix:
                window_counter[word1[r]] += 1
                if window_counter[word1[r]] == prefix_counter[word1[r]]:
                    all_success += 1
                r += 1
            if all_success == all_prefix:
                res += m - r + 1
            else:
                break
            window_counter[word1[l]] -= 1
            if window_counter[word1[l]] == prefix_counter[word1[l]] - 1:
                all_success -= 1
        return res

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.validSubstringCount("bcca", "abc"))  # 1
    print(solution.validSubstringCount(word1="abcabc", word2="abc"))  # 10
    print(solution.validSubstringCount(word1="abcabc", word2="aaabc"))  # 0
