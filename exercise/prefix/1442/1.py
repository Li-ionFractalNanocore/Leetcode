from typing import List
from collections import defaultdict


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        counter = defaultdict(list)
        result = 0
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
            for j in counter[prefix[i + 1]]:
                result += i - j
            counter[prefix[i]].append(i)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countTriplets([2, 3, 1, 6, 7])) # 4
    print(solution.countTriplets([1, 1, 1, 1, 1])) # 10
        