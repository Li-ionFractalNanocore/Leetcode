import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bit_count = max(nums).bit_length()
        counter = [0] * bit_count

        def accumulate(x, value=1):
            for i in range(bit_count):
                if x & (1 << i):
                    counter[i] += value

        def now():
            res = 0
            for i in range(bit_count):
                if counter[i] > 0:
                    res |= 1 << i
            return res
        
        j = 0
        result = float('inf')
        for i in range(n):
            while j < n:
                num_now = now()
                num_next = num_now | nums[j]
                if num_next >= k and i != j:
                    result = min(result, abs(num_next - k))
                    break
                else:
                    result = min(result, abs(num_next - k))
                    accumulate(nums[j])
                    j += 1
            accumulate(nums[i], -1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumDifference(nums = [1,2,4,5], k = 3)) # 0
    print(solution.minimumDifference(nums = [1,3,1,3], k = 2)) # 1
    print(solution.minimumDifference(nums = [1], k = 10)) # 9
                
