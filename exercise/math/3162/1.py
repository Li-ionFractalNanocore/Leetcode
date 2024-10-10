from collections import defaultdict
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        filtered_nums1 = [num // k for num in nums1 if num % k == 0]
        counter = defaultdict(int)
        for num in filtered_nums1:
            i = 1
            while i * i <= num:
                if num % i == 0:
                    counter[i] += 1
                    if num // i != i:
                        counter[num // i] += 1
                i += 1
        result = 0
        for num in nums2:
            result += counter[num]
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfPairs(nums1 = [4,60,120], nums2 = [10,20,4], k = 6)) # 4
    print(solution.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1)) # 5
    print(solution.numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3)) # 2