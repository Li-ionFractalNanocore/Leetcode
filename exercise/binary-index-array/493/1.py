from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        nums_extend = nums + [2 * x for x in nums]
        sorted_nums = sorted(set(nums_extend))
        mapping = {sorted_nums[i]: i + 1 for i in range(len(sorted_nums))}

        n = len(sorted_nums)
        bit = [0] * (n + 1)

        def update(x):
            while x <= n:
                bit[x] += 1
                x += x & -x

        def search(x):
            res = 0
            while x > 0:
                res += bit[x]
                x -= x & -x
            return res
        
        ans = 0
        for i in range(len(nums)):
            ans += i - search(mapping[nums[i] * 2])
            update(mapping[nums[i]])

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.reversePairs([2, 4, 3, 5, 1])) # 3