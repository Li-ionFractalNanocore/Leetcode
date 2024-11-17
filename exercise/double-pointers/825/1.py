from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = len(ages)
        ages.sort()
        l, r = 0, 0
        result = 0
        for age in ages:
            while l < n and ages[l] <= 0.5 * age + 7:
                l += 1
            while r < n and ages[r] <= age:
                r += 1
            if l < r:
                result += r - l - 1
        return result

        