from functools import cache
from itertools import accumulate

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        floor = list(map(int, floor))
        n = len(floor)
        f = list(accumulate(floor))
        for i in range(1, numCarpets + 1):
            g = [0] * n
            for j in range(carpetLen * i, n):
                g[j] = min(g[j - 1] + floor[j], f[j - carpetLen])
            f = g
        return f[-1]