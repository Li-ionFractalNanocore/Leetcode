from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        accum = 0
        min_value = float('inf')
        min_no = -1
        for i in range(n):
            accum += gas[i] - cost[i]
            if accum < min_value:
                min_value = accum
                min_no = (i + 1) % n
        if accum < 0:
            return -1
        return min_no
            

if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit([3,1,1], [1,2,2]))  # 0
    print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # 3