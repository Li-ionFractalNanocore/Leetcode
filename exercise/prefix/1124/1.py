from typing import List
import bisect


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hour_stack = [(0, -1)]

        diff_now = 0
        result = 0
        for i, hour in enumerate(hours):
            if hour > 8:
                diff_now += 1
            else:
                diff_now -= 1
            bisect_index = bisect.bisect_left(hour_stack, -diff_now + 1, key=lambda x: x[0])
            if bisect_index != len(hour_stack):
                result = max(result, i - hour_stack[bisect_index][1])
            if -diff_now > hour_stack[-1][0]:
                hour_stack.append((-diff_now, i))
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.longestWPI([6, 6, 9]))  # 1
    print(solution.longestWPI([9, 9, 6, 0, 6, 6, 9]))  # 3
            