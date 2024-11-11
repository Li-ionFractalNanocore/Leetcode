from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        length = len(cuts)

        dp = [[float('inf')] * length for _ in range(length)]
        for i in range(length - 1):
            dp[i][i + 1] = 0
        for l in range(2, length):
            for i in range(length - l):
                j = i + l
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
        return dp[0][length - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCost(7, [1, 3, 4, 5]))  # 16
        
        
        