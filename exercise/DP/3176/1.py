from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = 1
            for j in range(i):
                for l in range(k+1):
                    if nums[i] == nums[j]:
                        dp[i][l] = max(dp[i][l], dp[j][l] + 1)
                    elif l < k:
                        dp[i][l+1] = max(dp[i][l+1], dp[j][l] + 1)
        return max(max(dp[i]) for i in range(n))
                        

if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumLength([29,30,30], 0)) # 2
    print(solution.maximumLength([1,2,3,4,5,1], 0)) # 2
    print(solution.maximumLength([1,2,1,1,3], 2)) # 4
