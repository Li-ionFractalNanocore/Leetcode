from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = {}
        n = len(nums)
        mx = [0] * (n + 2)
        for num in nums:
            if num not in dp:
                dp[num] = [0] * (n + 1)
            for j in range(k, -1, -1):
                dp[num][j] = max(dp[num][j], mx[j]) + 1
                mx[j+1] = max(mx[j+1], dp[num][j])
        return mx[k+1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumLength([29,30,30], 0)) # 2
    print(solution.maximumLength([1,2,3,4,5,1], 0)) # 2
    print(solution.maximumLength([1,2,1,1,3], 2)) # 4