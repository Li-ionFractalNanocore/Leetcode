class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        coded_map = {0: -1}
        now = 0
        result = 0
        for i, c in enumerate(s):
            if c in idx_map:
                now ^= 1 << idx_map[c]
            if now in coded_map:
                result = max(result, i - coded_map[now])
            else:
                coded_map[now] = i
        return result