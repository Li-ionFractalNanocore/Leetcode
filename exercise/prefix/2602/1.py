from itertools import accumulate
from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        prefix_sum = list(accumulate(nums, initial=0))
        results = []
        for q in queries:
            idx = bisect_left(nums, q)
            left = idx * q - prefix_sum[idx]
            right = prefix_sum[n] - prefix_sum[idx] - (n - idx) * q
            results.append(left + right)
        return results
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.minOperations([3, 1, 6, 8], [1, 5]))  # [14, 10]