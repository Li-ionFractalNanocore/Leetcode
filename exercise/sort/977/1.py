from typing import List
import bisect


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        edge = bisect.bisect_left(nums, 0)
        l, r = edge - 1, edge
        while l >= 0 or r < n:
            if l < 0 or (r < n and nums[r] < -nums[l]):
                result.append(nums[r] ** 2)
                r += 1
            else:
                result.append(nums[l] ** 2)
                l -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortedSquares([-1]))  # [1]