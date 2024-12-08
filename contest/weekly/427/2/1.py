from typing import List


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points_set = set()
        for i in range(n):
            points_set.add((points[i][0], points[i][1]))
        results = -1
        for i in range(n):
            for j in range(i + 1, n):
                if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    flag = True
                    for k in range(n):
                        if k == i or k == j or (points[k][0] == x1 and points[k][1] == y2) or (points[k][0] == x2 and points[k][1] == y1):
                            continue
                        if min(x1, x2) <= points[k][0] <= max(x1, x2) and min(y1, y2) <= points[k][1] <= max(y1, y2):
                            flag = False
                            break
                    if flag:
                        results = max(results, abs(x1 - x2) * abs(y1 - y2))
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxRectangleArea([[1, 1], [1, 3], [3, 1], [3, 3]]))