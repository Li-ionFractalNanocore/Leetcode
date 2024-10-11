from typing import List
from collections import defaultdict
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        nums_counter = defaultdict(int)
        for num in nums:
            nums_counter[num] += 1
        gcd_counter = [0] * (max_num + 1)

        for gcd in range(max_num, 0, -1):
            counter = 0
            for gcd_multiple in range(gcd, max_num + 1, gcd):
                counter += nums_counter[gcd_multiple]
                gcd_counter[gcd] -= gcd_counter[gcd_multiple]
            gcd_counter[gcd] += (counter - 1) * counter // 2

        gcd_prefix = list(accumulate(gcd_counter))
        result = [bisect_right(gcd_prefix, q) for q in queries]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.gcdValues(nums = [2,3,4], queries = [0,2,2])) # [1,2,2]
