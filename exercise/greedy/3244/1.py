from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        next = [i + 1 for i in range(n)]
        length = n - 1

        results = []
        for l, r in queries:
            nxt = l
            while next[nxt] < r:
                length -= 1
                next[nxt], nxt = r, next[nxt]
            results.append(length)
        return results
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestDistanceAfterQueries(4, [[0, 3], [0, 2]]))  # [1, 1]
    print(solution.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]))  # [3, 2, 1]