from itertools import count


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0] * (k + 1)
        for i in count(1):
            for j in range(k, 0, -1):
                dp[j] += dp[j-1] + 1
            if dp[k] >= n:
                return i
        return -1
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.superEggDrop(3, 14))  # 4
    print(solution.superEggDrop(1, 2))  # 2
    print(solution.superEggDrop(2, 6))  # 3