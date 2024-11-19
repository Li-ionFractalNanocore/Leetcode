
from typing import List
import bisect


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        prefix = [0] * (n + 1)
        hour_stack = [0]
        for i, hour in enumerate(hours):
            prefix[i+1] = prefix[i] + (1 if hour > 8 else -1)
            if prefix[i+1] < prefix[hour_stack[-1]]:
                hour_stack.append(i+1)
        result = 0
        for i in range(n, -1, -1):
            while hour_stack and prefix[i] > prefix[hour_stack[-1]]:
                result = max(result, i - hour_stack[-1])
                hour_stack.pop()

        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.longestWPI([9, 9, 6, 0, 6, 6, 9]))  # 3