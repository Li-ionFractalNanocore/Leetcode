from typing import List


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        q = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = nums[i]
            q[i][i] = nums[i]
            for j in range(i+1, n):
                dp[i][j] = dp[i][j-1] ^ dp[i+1][j]
                q[i][j] = max(dp[i][j], q[i][j-1], q[i+1][j])
        result = []
        for l, r in queries:
            result.append(q[l][r])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSubarrayXor([2,8,4,32,16,1], [[0,2],[1,4],[0,5]])) # [12,60,60]
    print(solution.maximumSubarrayXor([0,7,3,2,8,5,1], [[0,3],[1,5],[2,4],[2,6],[5,6]])) # [7,14,11,14,5]