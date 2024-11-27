from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            alpha = ''.join(sorted(s))
            groups[alpha].append(s)
        return list(groups.values())
            
        