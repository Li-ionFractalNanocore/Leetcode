from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        first_max = [0] * n
        second_max = [0] * n
        first_window_sum, second_window_sum = 0, 0
        first_l, first_r = 0, 0
        result = 0
        for r in range(n):
            first_window_sum += nums[r]
            second_window_sum += nums[r]
            while r - first_l + 1 > firstLen:
                first_window_sum -= nums[first_l]
                first_l += 1
            first_max[r] = max(first_max[r-1], first_window_sum)
            while r - first_r + 1 > secondLen:
                second_window_sum -= nums[first_r]
                first_r += 1
            second_max[r] = max(second_max[r-1], second_window_sum)

            result = max(result, first_window_sum + second_max[r-firstLen] if r >= firstLen else 0, second_window_sum + first_max[r-secondLen] if r >= secondLen else 0)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))  # 20


