from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        exists = [0] * 26
        suffix_s = defaultdict(int)
        prefix_s = set()
        for i, c in enumerate(s):
            suffix_s[c] += 1
        
        for i, c in enumerate(s):
            suffix_s[c] -= 1
            for p in prefix_s:
                if suffix_s[p] > 0:
                    exists[ord(p) - ord('a')] |= 1 << (ord(c) - ord('a'))
            prefix_s.add(c)

        result = 0
        for i in range(26):
            result += int.bit_count(exists[i])
        
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPalindromicSubsequence("bbcbaba"))  # 4
    print(solution.countPalindromicSubsequence("aabca"))  # 3
        