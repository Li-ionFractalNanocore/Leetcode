class Solution:
    def checkRecord(self, n: int) -> int:
        f = [[0] * 2 for _ in range(3)]
        f[0][0] = 1
        for i in range(n):
            next_f = [[0] * 2 for _ in range(3)]
            for j in range(3):
                next_f[0][1] += f[j][0]
            for j in range(1, 3):
                for k in range(2):
                    next_f[j][k] += f[j-1][k]
            for j in range(2):
                next_f[0][j] += f[0][j] + f[1][j] + f[2][j]
            for j in range(3):
                for k in range(2):
                    f[j][k] = next_f[j][k] % 1000_000_007
        return sum(list(map(sum, f))) % 1000_000_007