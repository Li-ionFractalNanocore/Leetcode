from typing import List


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sorted = sorted([(num, i) for i, num in enumerate(nums)])
        res = n
        pre = -1
        for k, (now, i) in enumerate(nums_sorted):
            if i < pre:
                res += n - k
            pre = i
        return res

