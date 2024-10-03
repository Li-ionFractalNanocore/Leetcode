from typing import List


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        dp = [[float('inf')] * n for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]

        for t in range(maxTime + 1):
            for from_, to_, time_ in edges:
                if time_ <= t:
                    dp[t][from_] = min(dp[t - time_][to_] + passingFees[from_], dp[t][from_])
                    dp[t][to_] = min(dp[t - time_][from_] + passingFees[to_], dp[t][to_])
        
        res = min(dp[t][n - 1] for t in range(maxTime + 1))
        return -1 if res == float('inf') else res

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minCost(30, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]))  # 11