from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        diff = [num1 - num2 for num1, num2 in zip(nums1, nums2)]

        largest = 0
        largest_now = 0
        smallest = 0
        smallest_now = 0
        for num in diff:
            largest_now = max(largest_now, 0) + num
            largest = max(largest, largest_now)
            smallest_now = min(smallest_now, 0) + num
            smallest = min(smallest, smallest_now)
        
        return max(sum1, sum2, sum2 + largest, sum1 - smallest)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumsSplicedArray([60, 60, 60], [10, 90, 10]))  # 210