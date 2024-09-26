from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        n = len(points)
        for i in range(n):
            counter = defaultdict(int)
            for j in range(n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                result += counter[distance]
                counter[distance] += 1
        return result * 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfBoomerangs([[0,0],[1,0],[2,0]]))  # 2