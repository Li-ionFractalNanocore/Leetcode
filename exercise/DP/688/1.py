class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        rate = [[1.0] * n for _ in range(n)]
        ways = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for _ in range(k):
            new_rate = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dx, dy in ways:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            new_rate[i][j] += rate[x][y] / 8
            rate = new_rate
        
        return rate[row][column]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.knightProbability(3, 2, 0, 0))  # 0.0625

        