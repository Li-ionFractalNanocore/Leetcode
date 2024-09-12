from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        half = n // 2
        i = half - 1
        result = 0
        for j in range(n - 1, n - half - 1, -1):
            while i >= 0 and nums[i] * 2 > nums[j]:
                i -= 1
            if i >= 0:
                result += 2
                i -= 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxNumOfMarkedIndices([3,5,2,4]))  # 2
    print(solution.maxNumOfMarkedIndices([9,2,5,4]))  # 4
    print(solution.maxNumOfMarkedIndices([7,6,8]))  # 0
        