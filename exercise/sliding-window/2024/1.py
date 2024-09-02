class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        counter = {'T': 0, 'F': 0}
        l = 0
        result = 0
        for r in range(n):
            counter[answerKey[r]] += 1
            while counter['T'] > k and counter['F'] > k:
                counter[answerKey[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
            