from typing import List
from itertools import chain


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        k_counter = [0] * k
        k_full = 0
        all_nums = set(chain(*nums))
        nums_sorted = sorted(all_nums)
        num_mapping = {num: i for i, num in enumerate(nums_sorted)}

        n = len(nums_sorted)
        num_sets = [set() for _ in range(n)]
        for i in range(k):
            for num in nums[i]:
                num_sets[num_mapping[num]].add(i)
        
        result = 2 * 10 ** 5
        result_pair = None
        r = 0
        for l in range(n):
            while k_full < k and r < n:
                for k_index in num_sets[r]:
                    k_counter[k_index] += 1
                    if k_counter[k_index] == 1:
                        k_full += 1
                r += 1
            if k_full < k:
                break
            diff = nums_sorted[r - 1] - nums_sorted[l]
            if diff < result:
                result_pair = [nums_sorted[l], nums_sorted[r - 1]]
                result = diff
            for k_index in num_sets[l]:
                k_counter[k_index] -= 1
                if k_counter[k_index] == 0:
                    k_full -= 1
        
        return result_pair

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))  # [20,24]