from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        dp = [0] * n
        dp[-1] = max(0, -dungeon[-1][-1])
        for i in range(n - 2, -1, -1):
            dp[i] = max(0, dp[i + 1] - dungeon[-1][i])
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    dp[j] = max(0, dp[j] - dungeon[i][j])
                else:
                    dp[j] = max(0, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0] + 1

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # 7
            