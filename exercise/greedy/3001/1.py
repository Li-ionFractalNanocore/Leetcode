class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook_ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        bishop_ways = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for way in rook_ways:
            x, y = a, b
            m = 0
            touch = False
            while 1 <= x <= 8 and 1 <= y <= 8:
                if x == c and y == d:
                    break
                if x == e and y == f:
                    touch = True
                    break
                x += way[0]
                y += way[1]
                m += 1
            if touch:
                return 1
        
        for way in bishop_ways:
            x, y = c, d
            m = 0
            touch = False
            while 1 <= x <= 8 and 1 <= y <= 8:
                if x == a and y == b:
                    break
                if x == e and y == f:
                    touch = True
                    break
                x += way[0]
                y += way[1]
                m += 1
            if touch:
                return 1
        
        return 2

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minMovesToCaptureTheQueen(1, 1, 8, 8, 2, 3))  # 2
    print(solution.minMovesToCaptureTheQueen(5, 3, 3, 4, 5, 2))  # 1