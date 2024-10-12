from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        nums_counter = [0] * (101 + 1)

        def update(num: int, delta: int) -> None:
            real_num = num + 51
            while real_num < len(nums_counter):
                nums_counter[real_num] += delta
                real_num += real_num & -real_num
        
        def query(num: int) -> int:
            real_num = num + 51
            result = 0
            while real_num > 0:
                result += nums_counter[real_num]
                real_num -= real_num & -real_num
            return result
        
        result = []
        for i in range(k - 1):
            update(nums[i], 1)

        for l in range(n - k + 1):
            r = l + k
            update(nums[r - 1], 1)
            left, right = -50, 50
            while left < right:
                mid = (left + right) // 2
                if query(mid) < x:
                    left = mid + 1
                else:
                    right = mid
            if left < 0:
                result.append(left)
            else:
                result.append(0)
            update(nums[l], -1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2)) # [-1,-2,-2]
