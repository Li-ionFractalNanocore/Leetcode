from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        diff_nums = [num1 - num2 for num1, num2 in zip(nums1, nums2)]
        diff_set = set(diff_nums) | set([num - diff for num in diff_nums])
        n = len(diff_set)
        mapping = {x: i + 1 for i, x in enumerate(sorted(diff_set))}
        bit = [0] * (n + 1)

        def update(x):
            real_x = mapping[x]
            while real_x < len(bit):
                bit[real_x] += 1
                real_x += real_x & -real_x
        
        def query(x):
            real_x = mapping[x]
            ans = 0
            while real_x > 0:
                ans += bit[real_x]
                real_x -= real_x & -real_x
            return ans

        result = 0
        for i in range(len(diff_nums)):
            diff_num = diff_nums[i]
            result += query(diff_num)
            update(diff_num - diff)

        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfPairs([3, 2, 5], [2, 2, 1], 1)) # 3
        