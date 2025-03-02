from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        p_counter = defaultdict(int)
        s_counter = defaultdict(int)
        sat = 0
        for c in p:
            p_counter[c] += 1
        full = len(p_counter)
        result = []
        right = -1
        for left in range(n):
            while right + 1 < n and s_counter[s[right + 1]] < p_counter[s[right + 1]]:
                right += 1
                s_counter[s[right]] += 1
                if p_counter[s[right]] == s_counter[s[right]]:
                    sat += 1
            if sat == full:
                result.append(left)
            s_counter[s[left]] -= 1
            if s_counter[s[left]] == p_counter[s[left]] - 1:
                sat -= 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams(s = "cbaebabacd", p = "abc"))  # [0, 6]