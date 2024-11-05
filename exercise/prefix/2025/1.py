from itertools import accumulate
from collections import defaultdict

from typing import List

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = list(accumulate(nums))
        sum_nums = prefix_sum[-1]
        right_counter = defaultdict(int)
        for i in range(n - 1):
            right_counter[prefix_sum[i]] += 1
        
        result = 0
        if sum_nums % 2 == 0:
            result = right_counter[sum_nums // 2]

        left_counter = defaultdict(int)
        for i, num in enumerate(nums):
            delta = k - num
            if (sum_nums + delta) % 2 == 0:
                result = max(result, left_counter[(sum_nums + delta) // 2] + right_counter[(sum_nums - delta) // 2])
            left_counter[prefix_sum[i]] += 1
            right_counter[prefix_sum[i]] -= 1
        return result