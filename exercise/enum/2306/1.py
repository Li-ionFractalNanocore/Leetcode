from typing import List
from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffix_group = defaultdict(list)
        prefix_count = [0] * 26
        intersection = [[0] * 26 for _ in range(26)]

        for idea in ideas:
            prefix = idea[0]
            suffix = idea[1:]

            for p in suffix_group[suffix]:
                intersection[ord(p) - ord('a')][ord(prefix) - ord('a')] += 1
                intersection[ord(prefix) - ord('a')][ord(p) - ord('a')] += 1
            suffix_group[suffix].append(prefix)

            prefix_count[ord(prefix) - ord('a')] += 1

        result = 0
        for i in range(1, 26):
            for j in range(i):
                result += (prefix_count[i] - intersection[i][j]) * (prefix_count[j] - intersection[i][j])
        return result * 2

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.distinctNames(["coffee","donuts","time","toffee"]))  # 6
