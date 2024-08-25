from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for i in range(k):
            min_idx = -1
            for j, num in enumerate(nums):
                if min_idx == -1 or num < nums[min_idx]:
                    min_idx = j
            nums[min_idx] *= multiplier
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.getFinalState([2,1,3,5,6], 5, 2))  # [8, 4, 6, 5, 6]