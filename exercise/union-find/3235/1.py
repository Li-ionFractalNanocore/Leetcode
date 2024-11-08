from typing import List


class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)

        def in_circle(ox, oy, r, x, y):
            return (ox - x) ** 2 + (oy - y) ** 2 <= r ** 2

        visited = [False] * n
        def dfs(i):
            ox, oy, r = circles[i]
            if (
                oy <= Y
                and abs(ox - X) <= r
                or ox <= X
                and oy <= r
                or ox > X
                and in_circle(ox, oy, r, X, 0)
            ):
                return True
            visited[i] = True
            for j, (ox2, oy2, r2) in enumerate(circles):
                if (
                    not visited[j]
                    and (ox - ox2) ** 2 + (oy - oy2) ** 2 <= (r + r2) ** 2
                    and ox * r2 + ox2 * r < (r + r2) * X
                    and oy * r2 + oy2 * r < (r + r2) * Y
                    and dfs(j)
                ):
                    return True
            return False

        for i, (ox, oy, r) in enumerate(circles):
            if (
                in_circle(ox, oy, r, 0, 0)
                or in_circle(ox, oy, r, X, Y)
                or not visited[i]
                and (
                    ox <= X
                    and abs(oy - Y) <= r
                    or oy <= Y
                    and ox <= r
                    or oy > Y
                    and in_circle(ox, oy, r, 0, Y)
                )
                and dfs(i)
            ):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canReachCorner(5, 7, [[2, 2, 7]])) # True
    print(solution.canReachCorner(3, 4, [[2, 1, 1]])) # True
