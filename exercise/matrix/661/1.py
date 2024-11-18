from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                for i_delta in range(-1, 2):
                    for j_delta in range(-1, 2):
                        if 0 <= i + i_delta < m and 0 <= j + j_delta < n:
                            result[i][j] += img[i + i_delta][j + j_delta]
                            count += 1
                result[i][j] //= count
        return result
        