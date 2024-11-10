from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        def check(k):
            incresed = [False] * n
            increasing_len = 1
            if k == 1:
                incresed[0] = True
            for i in range(1, n):
                if nums[i] > nums[i - 1]:
                    increasing_len += 1
                else:
                    increasing_len = 1
                if increasing_len >= k:
                    incresed[i] = True
                    if i >= k and incresed[i - k]:
                        return True
            return False
        
        l, r = 1, n
        while l < r:
            m = (l + r + 1) // 2
            if check(m):
                l = m
            else:
                r = m - 1
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))  # 3
    print(solution.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))  # 2
        