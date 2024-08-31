from typing import List
import bisect


# tags: sliding window, binary search, prefix sum
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = []
        pre = [0] * (n + 1)
        i = 0
        counter = {'0': 0, '1': 0}
        for j in range(n):
            counter[s[j]] += 1
            while counter['0'] > k and counter['1'] > k:
                counter[s[i]] -= 1
                i += 1
            left.append(i)
            pre[j + 1] = pre[j] + (j - i + 1)
        
        results = []
        for l, r in queries:
            upper = bisect.bisect_left(left, l + 1, l, r + 1)
            result = (upper - l + 1) * (upper - l) // 2
            result += pre[r + 1] - pre[upper]
            results.append(result)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.countKConstraintSubstrings("010101", 1, [[0, 5], [1, 4], [2, 3]]))  # [15, 9, 3]
    print(solution.countKConstraintSubstrings("0001111", 2, [[0, 6]]))  # [26]


