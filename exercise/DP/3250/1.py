from typing import List
from itertools import accumulate


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        max_num = max(nums)
        dp = [i + 1 for i in range(max_num + 1)]
        for i in range(1, n):
            new_dp = [0] * (nums[i] + 1)
            for j in range(nums[i] + 1):
                pre = min(j, nums[i-1] - nums[i] + j)
                if pre >= 0:
                    new_dp[j] = dp[pre] % MOD
            dp = list(accumulate(new_dp))
        return dp[-1] % MOD

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.countOfPairs([2, 3, 2]))  # 4
    print(solution.countOfPairs([5, 5, 5, 5]))  # 126