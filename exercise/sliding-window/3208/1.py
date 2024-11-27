from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        l = 1 - k
        r = 2 - k
        result = 0
        while l <= n - k:
            while r < l + k and colors[r] != colors[r - 1]:
                r += 1
            if r == l + k:
                result += 1
                l += 1
            else:
                l = r
                r += 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfAlternatingGroups([0, 1, 0, 1, 0], 3))  # 3
        