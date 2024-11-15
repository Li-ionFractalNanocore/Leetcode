from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = float('-inf')
        counter = {}
        now = 0
        for i, num in enumerate(nums):
            now += num
            target = num - k
            if target in counter:
                result = max(result, now - counter[target])
            target = num + k
            if target in counter:
                result = max(result, now - counter[target])
            if num not in counter:
                counter[num] = now - num
            else:
                counter[num] = min(counter[num], now - num)
        return result if result != float('-inf') else 0
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSubarraySum([1, 2, 3, 4, 5, 6], 1))  # 11