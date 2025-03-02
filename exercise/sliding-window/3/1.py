class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        right = 0
        exists = set()
        exists.add(s[0])
        result = 0
        for left in range(n):
            while right + 1 < n and s[right + 1] not in exists:
                right += 1
                exists.add(s[right])
            result = max(result, right - left + 1)
            exists.remove(s[left])
        return result
        