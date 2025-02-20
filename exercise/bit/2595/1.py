from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        now = 0
        even, odd = 0, 0
        while n:
            if n & 1:
                if now & 1:
                    odd += 1
                else:
                    even += 1
            now += 1
            n >>= 1
        return [even, odd]
        
