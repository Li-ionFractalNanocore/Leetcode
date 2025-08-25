from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        m, n = len(mat), len(mat[0])
        l = m + n - 1
        direction = -1
        for i in range(l):
            direction = -direction
            if direction == 1:
                x = min(m - 1, i)
                y = i - x
            else:
                y = min(n - 1, i)
                x = i - y
            while 0 <= x < m and 0 <= y < n:
                result.append(mat[x][y])
                x -= direction
                y += direction
        return result


if __name__ == '__main__':
    s = Solution()
    mat = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
    print(s.findDiagonalOrder(mat))
    mat = [[i * 2 + j + 1 for j in range(2)] for i in range(2)]
    print(s.findDiagonalOrder(mat))