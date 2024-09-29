class Solution:
    def kthCharacter(self, k: int) -> str:
        start = "a"
        while len(start) < k:
            new_start = ""
            for c in start:
                if c == "z":
                    new_start += "a"
                else:
                    new_start += chr(ord(c) + 1)
            start = start + new_start
        return start[k-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthCharacter(10))