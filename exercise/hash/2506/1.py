from typing import List
from collections import defaultdict


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words_hash_counter = defaultdict(int)
        result = 0
        for word in words:
            word_hash = 0
            for c in word:
                word_hash |= 1 << (ord(c) - ord('a'))
            result += words_hash_counter[word_hash]
            words_hash_counter[word_hash] += 1
        return result
        
        