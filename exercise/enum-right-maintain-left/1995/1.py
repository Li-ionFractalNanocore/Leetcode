from typing import List
from collections import defaultdict


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        sum_counter = defaultdict(int)
        result = 0
        for b in range(1, n - 2):
            for a in range(b):
                sum_counter[nums[a] + nums[b]] += 1
            for d in range(b + 2, n):
                result += sum_counter[nums[d] - nums[b + 1]]
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.countQuadruplets([1, 2, 3, 6]))  # 1
                
                    