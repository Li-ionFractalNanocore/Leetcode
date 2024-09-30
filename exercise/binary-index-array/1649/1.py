from typing import List
from collections import defaultdict


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = max(instructions)
        nums = [0] * (n + 1)
        counter = defaultdict(int)

        def search(x: int) -> int:
            result = 0
            while x:
                result += nums[x]
                x -= x & -x
            return result

        def update(x: int):
            while x <= n:
                nums[x] += 1
                x += x & -x
        
        result = 0
        for i, instruction in enumerate(instructions):
            lower_and_equal = search(instruction)
            lower = lower_and_equal - counter[instruction]
            higher = i - lower_and_equal
            result = (result + min(lower, higher)) % (10 ** 9 + 7)
            update(instruction)
            counter[instruction] += 1

        return result