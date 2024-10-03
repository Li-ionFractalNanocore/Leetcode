from typing import List
from itertools import chain


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        max_x, max_y = max(x for x, y in rectangles), max(y for x, y in rectangles)
        mapping = {x: i for i, x in enumerate(sorted(set(x for x, y in chain(rectangles, points))))}
        n = len(mapping)
        counter = [[0] * (n + 1) for _ in range(max_y + 1)]
        line_counter = [0] * (max_y + 1)

        def update(x, y):
            for i in range(y + 1):
                line_counter[i] += 1
                num = mapping[x] + 1
                while num <= n:
                    counter[i][num] += 1
                    num += num & -num

        def search(x, y):
            res = 0
            x = mapping[x]
            while x:
                res += counter[y][x]
                x -= x & -x
            return res
        
        for x, y in rectangles:
            update(x, y)
        
        results = []
        for x, y in points:
            if x <= max_x and y <= max_y:
                results.append(line_counter[y] - search(x, y))
            else:
                results.append(0)
        
        return results 

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.countRectangles([[1,2],[2,3],[2,5]], [[2,1],[1,4]]))  # [2,1]