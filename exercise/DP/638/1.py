from typing import List
from functools import cache


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        filtered_special = []
        for s in special:
            sum_price = sum(s[i] * price[i] for i in range(n))
            if sum_price > s[-1]:
                filtered_special.append(s)

        @cache
        def dfs(needs):
            if all(need == 0 for need in needs):
                return 0
            result = sum(needs[i] * price[i] for i in range(n))
            for s in filtered_special:
                new_needs = [needs[i] - s[i] for i in range(n)]
                if all(need >= 0 for need in new_needs):
                    result = min(result, s[-1] + dfs(tuple(new_needs)))
            return result

        return dfs(tuple(needs))
        