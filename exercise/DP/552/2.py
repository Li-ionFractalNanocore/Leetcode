# Fast Exponentiation

class Solution:
    def matrixMul(self, a, b):
        m, n, o = len(a), len(a[0]), len(b[0])
        c = [[0] * o for _ in range(m)]
        for i in range(m):
            for j in range(o):
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]
                    c[i][j] %= 1000_000_007
        return c
    
    def fast_pow(self, a, n):
        res = [[0] * 6 for _ in range(6)]
        for i in range(6):
            res[i][i] = 1
        while n:
            if n & 1:
                res = self.matrixMul(res, a)
            a = self.matrixMul(a, a)
            n >>= 1
        return res

    def checkRecord(self, n: int) -> int:
        f = [[1], [0], [0], [0], [0], [0]]
        mat = [
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0]
               ]
        result = self.matrixMul(self.fast_pow(mat, n), f)
        return sum(map(sum, result)) % 1000_000_007

solution = Solution()
print(solution.checkRecord(2)) # 8
print(solution.checkRecord(1)) # 3
print(solution.checkRecord(10101)) # 183236316
print(solution.checkRecord(3)) # 19
