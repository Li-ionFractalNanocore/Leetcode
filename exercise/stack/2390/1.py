class Solution:
    def removeStars(self, s: str) -> str:
        chars = []
        for c in s:
            if c == '*':
                chars.pop()
            else:
                chars.append(c)
        return ''.join(chars)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.removeStars('abc**def'))  # adef