from typing import List
from random import randint


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        MOD = 1_017_017_017
        BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)
        n = len(target)
        power_base = [1] + [0] * n
        for i in range(n):
            power_base[i+1] = power_base[i] * BASE % MOD

        hash_map = set()
        for word in words:
            word_hash = 0
            for c in word:
                word_hash = (word_hash * BASE + ord(c)) % MOD
                hash_map.add(word_hash)

        now = 0
        count = 0
        window_hash = 0
        r = 0
        for i, c in enumerate(target):
            if i > 0:
                window_hash = (window_hash - ord(target[i-1]) * power_base[r - i]) % MOD
            while r < n and (window_hash * BASE + ord(target[r])) % MOD in hash_map:
                window_hash = (window_hash * BASE + ord(target[r])) % MOD
                r += 1
            if i == now:
                if i == r:
                    return -1
                count += 1
                now = r
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.minValidStrings(["abc","aaaaa","bcdef"], target="aabcdabc"))  # 3
    print(solution.minValidStrings(["abababab","ab"], target="ababaababa"))  # 2
    print(solution.minValidStrings(["abcdef"], target="xyz"))  # -1