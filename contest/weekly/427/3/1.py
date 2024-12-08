from typing import List
from collections import defaultdict


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        now = 0
        results = float('-inf')
        min_counter = {k - 1: 0}
        for i in range(n):
            now += nums[i]
            remain = i % k
            if remain in min_counter:
                results = max(results, now - min_counter[remain])
                min_counter[remain] = min(min_counter[remain], now)
            else:
                min_counter[remain] = now
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubarraySum([-1, -2, -3, -4, -5], 4))