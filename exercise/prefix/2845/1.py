from typing import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        counter = defaultdict(int)
        sum_ = 0
        result = 0
        for i, num in enumerate(nums):
            if num % modulo == k:
                sum_ += 1
            sum_mod = sum_ % modulo
            if sum_mod == k:
                result += 1
            target = (modulo + sum_mod - k) % modulo
            if target in counter:
                result += counter[target]
            counter[sum_mod] += 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.countInterestingSubarrays([3,1,9,6], 3, 0))
    print(solution.countInterestingSubarrays([3,2,4], 2, 1))
        