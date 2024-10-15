import math

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def cal(a, b):
            n = int(math.sqrt(a))
            for i in range(1, n+1):
                if (1 + i) * i > b:
                    return 2 * i - 1
            return 2 * n
        
        return max(cal(red, blue), cal(blue, red))


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxHeightOfTriangle(2, 4)) # 3