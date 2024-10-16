from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(set(nums))
        mapping = {sorted_num[i]: i + 1 for i in range(len(sorted_num))}

        n = len(nums)
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

        ans = [0] * n
        for i in range(n - 1, -1, -1):
            ans[i] = search(mapping[nums[i]] - 1)
            update(mapping[nums[i]])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSmaller([5, 2, 6, 1])) # [2, 1, 1, 0]