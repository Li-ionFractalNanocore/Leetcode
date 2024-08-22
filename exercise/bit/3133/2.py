class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        i, j = 0, 0
        while (n >> j) != 0:
            if x >> i & 1 == 0:
                x |= (n >> j & 1) << i
                j += 1
            i += 1
        return x


solution = Solution()
print(solution.minEnd(3, 4)) # 6
print(solution.minEnd(2, 7)) # 15
        
        