from typing import List
from sortedcontainers import SortedSet

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = SortedSet()
        result = []
        for i in range(n):
            window.add((-nums[i], i))
            if len(window) == k:
                result.append(-window[0][0])
                window.remove((-nums[i - k + 1], i - k + 1))
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
        