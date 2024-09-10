from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        greater = [0] * n
        greater[n - 1] = [0] * (n + 1)

        for k in range(n - 2, -1, -1):
            greater[k] = greater[k + 1].copy()
            for x in range(nums[k+1]):
                greater[k][x] += 1
        
        result = 0
        for j in range(1, n - 2):
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    less_r = n - 1 - j - greater[j][nums[k]]
                    less_l = nums[k] - less_r
                    result += less_l * greater[k][nums[j]]
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.countQuadruplets([1,3,2,4,5]))  # 2
    print(solution.countQuadruplets([1,2,3,4]))  # 0