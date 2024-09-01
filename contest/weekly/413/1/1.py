class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        coordinate1_x = ord(coordinate1[0]) - ord('a')
        coordinate1_y = ord(coordinate1[1]) - ord('1')
        coordinate2_x = ord(coordinate2[0]) - ord('a')
        coordinate2_y = ord(coordinate2[1]) - ord('1')
        return (coordinate1_x + coordinate1_y) % 2 == (coordinate2_x + coordinate2_y) % 2

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.checkTwoChessboards("a1", "c3"))  # True
    print(solution.checkTwoChessboards("a1", "h3"))  # False