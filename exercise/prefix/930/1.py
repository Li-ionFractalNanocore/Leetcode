from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        now = 0
        counter = defaultdict(int)
        counter[0] = 1
        result = 0
        for num in nums:
            now += num
            delta = now - goal
            result += counter[delta]
            counter[now] += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2))  # 4
        