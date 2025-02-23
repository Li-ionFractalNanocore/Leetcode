class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        digits = [int(c) for c in s]
        for i in range(n - 2):
            new_digits = []
            for j in range(n - i - 1):
                new_digits.append((digits[j] + digits[j + 1]) % 10)
            digits = new_digits
        return digits[0] == digits[1]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.hasSameDigits("3902"))
    print(solution.hasSameDigits("34789"))