from typing import List
from queue import PriorityQueue


class Item:
    def __init__(self, value, index, base):
        self.value = value
        self.index = index
        self.exp = 0
        self.base = base

    def add(self):
        self.exp += 1

    def __lt__(self, other):
        min_exp = min(self.exp, other.exp)
        exp_a = self.exp - min_exp
        exp_b = other.exp - min_exp
        if self.value * self.base ** exp_a < other.value * other.base ** exp_b:
            return True
        elif self.value * self.base ** exp_a == other.value * other.base ** exp_b:
            return self.index < other.index
        return False


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums

        n = len(nums)

        min_num, max_num = min(nums), max(nums)
        c = 0
        while min_num < max_num:
            min_num *= multiplier
            c += 1
        m = max(k // n - c, 0)
        k = k - m * n

        num_queue = PriorityQueue()

        for i, num in enumerate(nums):
            num_queue.put(Item(num, i, multiplier))

        for _ in range(k):
            item = num_queue.get()
            item.add()
            num_queue.put(item)

        MOD = 10 ** 9 + 7
        def fast_exp(base, exp):
            result = 1
            while exp:
                if exp & 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result
        
        result = [0] * n
        while not num_queue.empty():
            item = num_queue.get()
            result[item.index] = item.value * fast_exp(item.base, item.exp + m) % MOD
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getFinalState([2,1,3,5,6], 5, 2))  # [8,4,6,5,6]
    print(solution.getFinalState([100000,2000], 2, 1000000))  # [999999307,999999993]
    print(solution.getFinalState([2, 10000], 1000000, 10))

