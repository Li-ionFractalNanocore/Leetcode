from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        now = 0
        result = 0
        prefix_counter = defaultdict(int)
        prefix_counter[0] = 1
        for i, s in enumerate(word):
            now = now ^ (1 << (ord(s) - ord('a')))
            for j in range(10):
                result += prefix_counter[now ^ (1 << j)]
            result += prefix_counter[now]
            prefix_counter[now] += 1
        return result
