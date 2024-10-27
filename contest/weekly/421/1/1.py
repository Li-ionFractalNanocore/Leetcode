from typing import List
from functools import cache


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)
        
        prefix_gcd = [0] * n 
        prefix_lcm = [0] * n
        prefix_gcd[0] = nums[0]
        prefix_lcm[0] = nums[0]
        for i in range(1, n):
            new_gcd = gcd(prefix_gcd[i-1], nums[i])
            new_lcm = lcm(prefix_lcm[i-1], nums[i])
            prefix_gcd[i] = new_gcd
            prefix_lcm[i] = new_lcm

        suffix_gcd = [0] * n
        suffix_lcm = [0] * n
        suffix_gcd[-1] = nums[-1]
        suffix_lcm[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            new_gcd = gcd(suffix_gcd[i + 1], nums[i])
            new_lcm = lcm(suffix_lcm[i + 1], nums[i])
            suffix_gcd[i] = new_gcd
            suffix_lcm[i] = new_lcm

        ans = prefix_gcd[-1] * prefix_lcm[-1]
        if n == 1:
            return ans
        for i in range(n):
            if i == 0:
                ans = max(ans, suffix_gcd[1] * suffix_lcm[1])
                continue
            if i == n - 1:
                ans = max(ans, prefix_gcd[-2] * prefix_lcm[-2])
                continue
            new_gcd = gcd(prefix_gcd[i - 1], suffix_gcd[i + 1])
            new_lcm = lcm(prefix_lcm[i - 1], suffix_lcm[i + 1])
            ans = max(ans, new_gcd * new_lcm)

        return ans

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore([2, 4, 8, 16]))
        