from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        sum_all = sum(arr)
        result = 0
        if k >= 2:
            arr = arr * 2
        sum_now = 0
        end = -1
        for i, num in enumerate(arr):
            if num > sum_now + num:
                sum_now = num
            else:
                sum_now += num
            if sum_now > result:
                result = sum_now
                end = i
        if end >= n and sum_all > 0:
            return (result + sum_all * (k - 2)) % MOD
        else:
            return result % MOD

            
if __name__ == '__main__':
    solution = Solution()
    print(solution.kConcatenationMaxSum([1, 2], 3))  # 9
    print(solution.kConcatenationMaxSum([1, -2, 1], 5))  # 2
    print(solution.kConcatenationMaxSum([-1, -2], 7))  # 0
        