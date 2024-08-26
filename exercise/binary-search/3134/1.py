from typing import List
from collections import defaultdict


# tags: binary search, sliding window
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)

        def count(x):
            counter = defaultdict(int)
            counter[nums[0]] = 1
            counting = 1
            r = 0
            results = 0
            for l in range(n):
                while r < n - 1 and counting + int(counter[nums[r+1]] == 0) <= x:
                    r += 1
                    counter[nums[r]] += 1
                    if counter[nums[r]] == 1:
                        counting += 1
                results += r - l + 1
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    counting -= 1
            return results

        left, right = 1, len(nums)
        target = ((n + 1) * n // 2 + 1) // 2
        while left < right:
            mid = left + (right - left) // 2
            val = count(mid)
            if val < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.medianOfUniquenessArray([1, 2, 3]))  # 1
    print(solution.medianOfUniquenessArray([3, 4, 3, 4, 5]))  # 2
    print(solution.medianOfUniquenessArray([4, 3, 5, 4]))  # 2