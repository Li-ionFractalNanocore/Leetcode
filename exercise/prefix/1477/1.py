from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        dp = [float('inf')] * len(arr)
        now = 0
        result = float('inf')
        for i, num in enumerate(arr):
            now += num
            delta = now - target
            if delta in prefix:
                dis = i - prefix[delta]
                if i - dis >= 0:
                    result = min(result, dis + dp[i-dis])
            else:
                dis = float('inf')
            if i > 0:
                dp[i] = min(dp[i-1], dis)
            else:
                dp[i] = dis
            prefix[now] = i
        return result if result != float('inf') else -1
            
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minSumOfLengths([3, 2, 2, 4, 3], 3))