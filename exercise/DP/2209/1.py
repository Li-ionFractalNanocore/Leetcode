from functools import cache

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:

        @cache
        def cover(num, index):
            if num == 0:
                return sum([1 for i in range(index + 1) if floor[i] == '1'])
            if index < 0:
                return 0
            return min(cover(num, index - 1) + int(floor[index] == '1'), cover(num - 1, index - carpetLen))
        
        return cover(numCarpets, len(floor) - 1)

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumWhiteTiles(floor="10110101", numCarpets=2, carpetLen=2))
        