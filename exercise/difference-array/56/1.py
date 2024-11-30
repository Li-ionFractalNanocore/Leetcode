from typing import List
from itertools import accumulate


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max([interval[1] for interval in intervals])
        diff = [0] * (max_val + 2)
        point = [0] * (max_val + 2)
        for interval in intervals:
            diff[interval[0]] += 1
            diff[interval[1]] -= 1
            if interval[0] == interval[1]:
                point[interval[0]] += 1
        real = list(accumulate(diff))
        result = []
        start = -1
        for i in range(max_val + 2):
            if real[i] > 0 and start == -1:
                start = i
            if real[i] == 0 and start != -1:
                result.append([start, i])
                start = -1
                if point[i] > 0:
                    point[i] = 0
            if real[i] == 0 and point[i] > 0:
                result.append([i, i])
        return result

        