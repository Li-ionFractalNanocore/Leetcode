class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        result = 1
        now = 1
        for i in range(1, n):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                now += 1
                result = max(result, now)
            else:
                now = 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.longestContinuousSubstring("abacaba")) # 2