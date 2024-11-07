from typing import List
from collections import defaultdict
from itertools import accumulate


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = defaultdict(list)
        for i, num in enumerate(nums):
            counter[num].append(i)
        results = [0] * n

        for l in counter:
            prefix = list(accumulate(counter[l], initial=0))
            m = len(counter[l])
            for i, idx in enumerate(counter[l]):
                results[idx] = (idx * (i + 1) - prefix[i + 1]) + (prefix[m] - prefix[i + 1] - (m - i - 1) * idx)
        return results

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.distance([1, 3, 1, 1, 2]))  # [5, 0, 3, 4, 0]
        