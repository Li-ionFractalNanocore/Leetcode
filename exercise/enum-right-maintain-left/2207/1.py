class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = len(text)
        counter = {pattern[0]: 0, pattern[1]: 0}
        result = 0
        for i in range(n):
            if text[i] == pattern[1]:
                result += counter[pattern[0]]
            if text[i] in counter:
                counter[text[i]] += 1
        return result + max(counter[pattern[0]], counter[pattern[1]])

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSubsequenceCount("abdcdbc", "ac"))  # 4