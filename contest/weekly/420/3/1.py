from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                divisor = 2
                while divisor * divisor <= nums[i]:
                    if nums[i] % divisor == 0:
                        nums[i] = divisor
                        break
                    divisor += 1
                if nums[i] > nums[i+1]:
                    return -1
        return cnt

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minOperations([6, 7, 10])) # 0
    print(solution.minOperations([25, 7])) # 1
    print(solution.minOperations([7, 7, 6])) # -1
    print(solution.minOperations([1, 1, 1, 1])) # 0
        