from typing import List


# 183ms
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key=lambda x: (-x[0]))
        n = len(rectangles)
        max_y = max(y for x, y in rectangles)
        counter = [0] * (max_y + 1)

        def update(x):
            while x <= max_y:
                counter[x] += 1
                x += x & -x

        def search(x):
            res = 0
            while x:
                res += counter[x]
                x -= x & -x
            return res

        results = [0] * len(points)
        j = 0
        for i, (x, y) in sorted(zip(range(len(points)), points), key=lambda x: (-x[1][0])):
            while j < n and rectangles[j][0] >= x:
                update(rectangles[j][1])
                j += 1
            if y <= max_y:
                results[i] = j - search(y - 1)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.countRectangles([[1,2],[2,3],[2,5]], [[2,1],[1,4]]))  # [2,1]