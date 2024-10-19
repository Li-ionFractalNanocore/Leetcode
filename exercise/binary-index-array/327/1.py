from typing import List
from itertools import accumulate


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = list(accumulate(nums, initial=0))
        prefix_sum_set = set(prefix_sum)
        all_nums = prefix_sum_set | set([prefix -lower for prefix in prefix_sum_set]) | set([prefix - upper - 1 for prefix in prefix_sum_set])
        mapping = {x: i + 1 for i, x in enumerate(sorted(all_nums))}
        
        bit = [0] * (len(mapping) + 1)
        
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
        update(0)
        for i in range(len(nums)):
            all_sum = prefix_sum[i+1]
            upper_bound = all_sum - upper
            lower_bound = all_sum - lower
            cnt = query(lower_bound) - query(upper_bound - 1)
            result += cnt
            update(all_sum)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countRangeSum([-2, 5, -1], -2, 2)) # 3

        