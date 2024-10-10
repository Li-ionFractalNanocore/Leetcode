from collections import defaultdict
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1_counter = defaultdict(int)
        nums2_counter = defaultdict(int)
        for num in nums1:
            if num % k == 0:
                nums1_counter[num // k] += 1
        if len(nums1_counter) == 0:
            return 0
        for num in nums2:
            nums2_counter[num] += 1

        upper_bound = max(nums1_counter.keys())
        result = 0
        for num in nums2_counter.keys():
            for num_iter in range(num, upper_bound + 1, num):
                if num_iter in nums1_counter:
                    result += nums1_counter[num_iter] * nums2_counter[num]
        return result
        

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfPairs(nums1 = [4,60,120], nums2 = [10,20,4], k = 6)) # 4
    print(solution.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1)) # 5
    print(solution.numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3)) # 2