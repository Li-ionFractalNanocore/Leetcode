from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        now = -1
        last = [-1] * n
        next_ = [-1] * n
        counter = [0] * n
        for i, c in enumerate(s):
            if c == '|':
                now = i
            counter[i] = counter[i-1]
            if c == '*':
                counter[i] += 1
            last[i] = now
        now = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                now = i
            next_[i] = now
        result = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            l_candle = next_[l]
            r_candle = last[r]
            if l_candle == -1 or r_candle == -1 or l_candle >= r_candle:
                result[i] = 0
            else:
                result[i] = counter[r_candle] - counter[l_candle]
        return result
            

        