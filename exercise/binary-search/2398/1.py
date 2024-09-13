from typing import List
from itertools import accumulate
from collections import deque


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        prefix_sum = list(accumulate(runningCosts, initial=0))

        def check(k):
            if k == 0:
                return True
            max_stack = deque()
            for i in range(k):
                while len(max_stack) > 0 and max_stack[-1] < chargeTimes[i]:
                    max_stack.pop()
                max_stack.append(chargeTimes[i])
            if max_stack[0] + k * (prefix_sum[k] - prefix_sum[0]) <= budget:
                return True
            for i in range(1, n - k + 1):
                j = i + k - 1
                if max_stack[0] == chargeTimes[i - 1]:
                    max_stack.popleft()
                while len(max_stack) > 0 and max_stack[-1] < chargeTimes[j]:
                    max_stack.pop()
                max_stack.append(chargeTimes[j])
                if max_stack[0] + k * (prefix_sum[j+1] - prefix_sum[i]) <= budget:
                    return True
            return False

        l, r = 0, n
        while l < r:
            m = (l + r + 1) // 2
            if check(m):
                l = m
            else:
                r = m - 1
        return l

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumRobots([11,12,19], [10,8,7], 19))  # 0
    print(solution.maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25))  # 3