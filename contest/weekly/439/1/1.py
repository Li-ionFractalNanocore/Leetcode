from typing import List
from collections import defaultdict


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = defaultdict(int)
        for i in range(n - k + 1):
            sub_set = set(nums[i:i + k])
            for num in sub_set:
                counter[num] += 1
        max_num = -1
        for k, v in counter.items():
            if v == 1:
                max_num = max(max_num, k)
        return max_num


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestInteger(nums = [3,9,2,1,7], k = 3))  # 7
    print(solution.largestInteger(nums = [3,9,7,2,1,7], k = 4))  # 3
    print(solution.largestInteger(nums = [0, 0], k = 2))  # 0
    print(solution.largestInteger(nums = [0, 0], k = 1))  # -1