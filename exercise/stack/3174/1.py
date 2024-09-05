class Solution:
    def clearDigits(self, s: str) -> str:
        non_digit = []
        for c in s:
            if c.isdigit():
                non_digit.pop()
            else:
                non_digit.append(c)
        return ''.join(non_digit)


if __name__ == '__main__':
    solution = Solution()
    print(solution.clearDigits('abc123')) #
    print(solution.clearDigits('abc')) # abc
    print(solution.clearDigits('abc12c3')) # a