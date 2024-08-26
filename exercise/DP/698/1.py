from typing import List
from functools import cache


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        target = nums_sum // k
        nums.sort()

        @cache
        def dfs(state, now):
            if state == 0:
                return True
            for i in range(n):
                if now + nums[i] > target:
                    break
                if state & (1 << i) and dfs(state ^ (1 << i), (now + nums[i]) % target):
                    return True
            return False

        return dfs((1 << n) - 1, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # True
    print(solution.canPartitionKSubsets([1, 2, 3, 4], 3))  # False
    print(solution.canPartitionKSubsets([1, 1, 2, 4], 4))  # False