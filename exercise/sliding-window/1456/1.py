class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        result = 0
        for i in range(n):
            if s[i] in 'aeiou':
                count += 1
            if i >= k:
                if s[i-k] in 'aeiou':
                    count -= 1
            result = max(result, count)
        return result