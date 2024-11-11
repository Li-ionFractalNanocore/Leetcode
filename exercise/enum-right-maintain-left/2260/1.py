from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        record = dict()
        result = len(cards) + 1
        for i, card in enumerate(cards):
            if card in record:
                result = min(result, i - record[card] + 1)
            record[card] = i
        
        return result if result != len(cards) + 1 else -1