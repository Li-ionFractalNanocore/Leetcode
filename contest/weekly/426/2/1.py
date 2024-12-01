from typing import List
from bisect import bisect_left


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        sum_nums = sum(nums)
        for i in range(n - 1, -1, -1):
            num = nums[i]
            remain = sum_nums - num
            if remain % 2 == 1:
                continue
            find = remain // 2
            idx = bisect_left(nums, find)
            if idx < n and idx != i and nums[idx] == find:
                return num
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.getLargestOutlier([1, 1, 1, 1, 1, 5, 5]))  # 5
    print(solution.getLargestOutlier([2, 3, 5, 10]))  # 10
    print(solution.getLargestOutlier([-2, -1, -3, -6, 4]))  # 4