from typing import List
from collections import defaultdict


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        row_counter = defaultdict(int)
        for i in range(n):
            row_counter[board[0][i]] += 1
        if abs(row_counter[0] - row_counter[1]) > 1:
            return -1

        col_counter = defaultdict(int)
        for i in range(n):
            col_counter[board[i][0]] += 1
        if abs(col_counter[0] - col_counter[1]) > 1:
            return -1

        for i in range(1, n):
            diff = 0
            for j in range(n):
                if board[j][0] != board[j][i]:
                    diff += 1
            if diff != 0 and diff != n:
                return -1
        
        def count(line, counter):
            x0 = 1 if counter[1] > counter[0] else 0
            c = 0
            for i in range(n):
                if line[i] != x0:
                    c += 1
                x0 = 1 - x0
            return c // 2 if n % 2 else min(c // 2, (n - c) // 2)
        
        return count(board[0], row_counter) + count([board[i][0] for i in range(n)], col_counter)
                

        