from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        now = 0
        counter = 0
        for i in range(1, n):
            if skills[i] > skills[now]:
                now = i
                counter = 1
            else:
                counter += 1
            if counter == k:
                return now
        return now
        