from typing import List


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        power = [1] * n
        for i in range(n - 1):
            power[i + 1] = (power[i] * 10) % k

        end = (n + 1) // 2
        visited = [[False] * k for _ in range(end + 1)]
        result = [""] * n

        def dfs(pos, m):
            if pos == end:
                return m == 0
            visited[pos][m] = True
            for i in range(9, -1, -1):
                if n % 2 == 1 and pos == end - 1:
                    next_m = (i * power[pos] + m) % k
                else:
                    next_m = ((i * power[pos] + i * power[n - 1 - pos]) % k + m) % k
                if not visited[pos+1][next_m] and dfs(pos+1, next_m):
                    result[pos] = str(i)
                    result[n-1-pos] = str(i)
                    return True

        dfs(0, 0)
        return "".join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestPalindrome(5, 6))  # 89898
    print(solution.largestPalindrome(3, 5))  # 595
    print(solution.largestPalindrome(1, 4))  # 8
