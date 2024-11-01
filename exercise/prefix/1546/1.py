from typing import List
from itertools import accumulate


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sum_now = 0
        prefix_set = set()
        prefix_set.add(0)
        result = 0
        for num in nums:
            sum_now += num
            if sum_now - target in prefix_set:
                prefix_set.clear()
                prefix_set.add(0)
                sum_now = 0
                result += 1
            else:
                prefix_set.add(sum_now)
        return result
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxNonOverlapping([1,1,1,1,1], 2))
    print(solution.maxNonOverlapping([-1,3,5,1,4,2,-9], 6))
    print(solution.maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10))