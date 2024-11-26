from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        result = 0
        for i in range(-1, n - 1):
            if colors[i-1] == 1 - colors[i] and colors[i] == 1 - colors[i+1]:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfAlternatingGroups([1, 1, 1]))  # 0
    print(solution.numberOfAlternatingGroups([0, 1, 0, 0, 1]))  # 3
            
        