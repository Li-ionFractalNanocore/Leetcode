class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        position = {c: i for i, c in enumerate(s)}
        result = 0
        for i, c in enumerate(t):
            result += abs(i - position[c])
        return result


solution = Solution()
print(solution.findPermutationDifference("abc", "bac"))  # 2
print(solution.findPermutationDifference("abcde", "edbac"))  # 12
