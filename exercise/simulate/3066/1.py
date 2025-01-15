from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        while nums[0] < k:
            a, b = heapq.heappop(nums), heapq.heappop(nums)
            new_val = min(a, b) * 2 + max(a, b)
            heapq.heappush(nums, new_val)
        return n - len(nums)

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([2,11,10,1,3], 10))  # 2
            
        