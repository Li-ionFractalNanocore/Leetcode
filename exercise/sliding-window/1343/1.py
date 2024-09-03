from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        n = len(arr)
        sum_ = 0
        for i in range(n):
            sum_ += arr[i]
            if i < k - 1:
                continue
            if sum_ >= k * threshold:
                result += 1
            sum_ -= arr[i - k + 1]
        return result
