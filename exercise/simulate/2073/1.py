from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        result = 0
        upper = tickets[k]
        for i in range(n):
            if i <= k:
                result += min(tickets[i], upper)
            else:
                result += min(tickets[i], upper - 1)
        return result