from collections import defaultdict

# tags: DP
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            counter = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                counter[s[j]] += 1
                max_cnt = max(max_cnt, counter[s[j]])
                if i - j + 1 == max_cnt * len(counter):
                    dp[i+1] = min(dp[i+1], dp[j] + 1)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumSubstringsInPartition("fabccddg"))  #3