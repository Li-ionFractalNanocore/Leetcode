from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        diff_counter = {0: 1}
        diff_now = 0
        has_k = False
        result = 0
        for num in nums:
            if num == k:
                has_k = True
            elif num > k:
                diff_now += 1
            else:
                diff_now -= 1
            if has_k:
                result += diff_counter.get(diff_now, 0) + diff_counter.get(diff_now - 1, 0)
            else:
                diff_counter[diff_now] = diff_counter.get(diff_now, 0) + 1
        return result

        