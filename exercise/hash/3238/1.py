from typing import List
from collections import defaultdict


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        result = 0
        counter = defaultdict(lambda : [0] * 11)
        win = set()
        for x, y in pick:
            if x in win:
                continue
            counter[x][y] += 1
            if counter[x][y] == x + 1:
                result += 1
                win.add(x)
        return result
        