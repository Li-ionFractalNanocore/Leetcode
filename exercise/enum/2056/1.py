from typing import List


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        EDGE = 8
        n = len(pieces)

        path = [None] * n

        def generate_all_moves(x0, y0, ways):
            moves = [(x0, y0, 0, 0, 0)]
            for dx, dy in ways:
                x, y = x0 + dx, y0 + dy
                m = 1
                while 1 <= x <= EDGE and 1 <= y <= EDGE:
                    moves.append((x0, y0, dx, dy, m))
                    x += dx
                    y += dy
                    m += 1
            return moves

        rook_ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        bishop_ways = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        queen_ways = rook_ways + bishop_ways
        ways = {'rook': rook_ways, 'bishop': bishop_ways, 'queen': queen_ways}
        all_moves = []
        for i, piece in enumerate(pieces):
            all_moves.append(generate_all_moves(positions[i][0], positions[i][1], ways[piece]))

        def is_valid(move1, move2):
            x1, y1, dx1, dy1, m1 = move1
            x2, y2, dx2, dy2, m2 = move2
            for i in range(max(m1, m2)):
                if i < m1:
                    x1 += dx1
                    y1 += dy1
                if i < m2:
                    x2 += dx2
                    y2 += dy2
                if x1 == x2 and y1 == y2:
                    return False
            return True

        def dfs(i):
            if i == n:
                return 1
            result = 0
            for move_now in all_moves[i]:
                if all(is_valid(move_now, move) for move in path[:i]):
                    path[i] = move_now
                    result += dfs(i + 1)
            return result

        return dfs(0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countCombinations(["rook"], [[1, 1]]))  # 15
    print(solution.countCombinations(["queen"], [[1, 1]]))  # 22
    print(solution.countCombinations(["bishop"], [[4, 3]]))  # 12
    print(solution.countCombinations(["rook", "rook"], [[1, 1], [8, 8]]))  # 223
    print(solution.countCombinations(["queen", "bishop"], [[5, 7], [3, 4]]))  # 281

                    
            
        