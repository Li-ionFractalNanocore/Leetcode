from typing import List
from itertools import accumulate


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = list(accumulate(nums, initial=0))

        result = float('inf')
        for i in range(n):
            for j in range(i + l, min(i + r + 1, n + 1)):
                re = prefix[j] - prefix[i]
                if re > 0:
                    result = min(result, re)
        return result if result != float('inf') else -1
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumSumSubarray([-12, 8], 1, 1))  # 4
    print(solution.minimumSumSubarray([4, -10], 1, 1))  # 4