from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cnt = 0
        x, y = -1, -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        for dx, dy in rook_ways:
            new_x, new_y = x + dx, y + dy
            while 0 <= new_x < 8 and 0 <= new_y < 8:
                if board[new_x][new_y] == 'B':
                    break
                if board[new_x][new_y] == 'p':
                    cnt += 1
                    break
                new_x += dx
                new_y += dy
        return cnt
