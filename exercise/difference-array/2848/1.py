from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        m = 100
        diff = [0] * (m + 1)
        n = len(nums)
        for start, end in nums:
            diff[start] += 1
            diff[end+1] -= 1
        now = 0
        result = 0
        for i in range(m+1):
            now = now + diff[i]
            if now > 0:
                result += 1
        return result