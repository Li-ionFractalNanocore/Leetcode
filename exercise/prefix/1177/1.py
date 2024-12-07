from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(s[i]) - ord('a')))
        
        results = []
        for f, t, k in queries:
            alpha_count = prefix[t + 1] ^ prefix[f]
            odd_count = alpha_count.bit_count()
            if odd_count <= 2 * k + 1:
                results.append(True)
            else:
                results.append(False)
        return results

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.canMakePaliQueries("abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))  # [True, False, False, True, True]
        