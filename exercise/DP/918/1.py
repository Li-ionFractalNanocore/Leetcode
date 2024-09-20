from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_res = nums[0]
        sum_nums = sum(nums)
        min_res = nums[0]
        min_all = nums[0]
        max_all = nums[0]

        for i in range(1, n):
            max_res = max(max_res + nums[i], nums[i])
            max_all = max(max_all, max_res)

            min_res = min(min_res + nums[i], nums[i])
            min_all = min(min_all, min_res)
        
        if min_all == sum_nums:
            return max_all
        return max(max_all, sum_nums - min_all)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubarraySumCircular([1,-2,3,-2]))  # 3
    print(solution.maxSubarraySumCircular([5,-3,5]))  # 10
    print(solution.maxSubarraySumCircular([3,-2,2,-3]))  # 3