from typing import List
from collections import defaultdict


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = defaultdict(int)
        for p in power:
            counter[p] += p
        powers = sorted(counter.items())
        n = len(powers)
        f = [0] * n
        result = 0
        for i in range(n):
            f[i] = powers[i][1]
            if i > 0:
                if powers[i][0] > powers[i-1][0] + 2:
                    f[i] = max(f[i], f[i-1] + powers[i][1])
                else:
                    f[i] = max(f[i], f[i-1])
            if i > 1:
                if powers[i][0] > powers[i-2][0] + 2:
                    f[i] = max(f[i], f[i-2] + powers[i][1])
                else:
                    f[i] = max(f[i], f[i-2])
            if i > 2:
                f[i] = max(f[i], f[i-3] + powers[i][1])
            result = max(result, f[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumTotalDamage([1,1,3,4])) # 6
    print(solution.maximumTotalDamage([7,1,6,6])) # 13
