from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        value_dict = dict(zip(chars, vals))
        for i in range(26):
            c = chr(ord('a') + i)
            if c not in value_dict:
                value_dict[c] = i + 1
        result = 0
        f = 0
        for c in s:
            f = max(f + value_dict[c], value_dict[c])
            result = max(result, f)
        return result
