from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        axis = ((0, 0), (0, 1), (1, 0), (1, 1))
        for from_x, from_y in axis:
            counter = {'W': 0, 'B': 0}
            for add_x, add_y in axis:
                counter[grid[from_x + add_x][from_y + add_y]] += 1
            if counter['W'] != counter['B']:
                return True
        return False

