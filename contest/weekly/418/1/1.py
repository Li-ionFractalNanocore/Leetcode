from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        max_result = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i == j or j == k or i == k:
                        continue
                    perm = [i, j, k]
                    result = 0
                    length_counter = 0
                    for l in range(n):
                        result += nums[perm[l]] << length_counter
                        length_counter += nums[perm[l]].bit_length()
                    if result > max_result:
                        max_result = result
        return max_result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxGoodNumber([1, 2, 3]))  # 30