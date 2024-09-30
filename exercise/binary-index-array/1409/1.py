from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        q = len(queries)
        n = m + q
        nums = [0] * (n + 1)
        indeces = [i for i in range(q + 1, n + 1)]

        def search(x: int) -> int:
            result = 0
            while x:
                result += nums[x]
                x -= x & -x
            return result

        def update(x: int, update_value: int):
            while x <= n:
                nums[x] += update_value
                x += x & -x

        for index in indeces:
            update(index, 1)

        now = q
        result = []
        for query in queries:
            index = indeces[query - 1]
            result.append(search(index - 1))
            indeces[query - 1] = now
            now -= 1
            update(index, -1)
            update(indeces[query - 1], 1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.processQueries([3, 1, 2, 1], 5))  # [2, 1, 2, 1]