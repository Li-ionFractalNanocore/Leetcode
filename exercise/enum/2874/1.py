from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_max = [0] * n
        suffix_max[-1] = max(nums[-1], 0)
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        result = 0
        prefix_max = 0
        for i in range(n - 1):
            result = max(result, (prefix_max - nums[i]) * suffix_max[i + 1])
            prefix_max = max(prefix_max, nums[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumTripletValue([12,6,1,2,7]))  # 77