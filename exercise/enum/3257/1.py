from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        suffix = [None] * m

        def update(row):
            for i, item in enumerate(row):
                exists = set()
                for k in range(3):
                    if item > p[k][0] and i not in exists:
                        p[k], (item, i) = (item, i), p[k]
                    exists.add(p[k][1])

        p = [(float('-inf'), -1)] * 3
        for i in range(m - 1, 0, -1):
            update(board[i])
            suffix[i] = p.copy()

        p = [(float('-inf'), -1)] * 3
        result = float('-inf')
        for i, row in enumerate(board[:-2]):
            update(row)
            for j2, num2 in enumerate(board[i+1]):
                for num1, j1 in p:
                    for num3, j3 in suffix[i+2]:
                        if j1 != j2 and j2 != j3 and j1 != j3:
                            result = max(result, num1 + num2 + num3)
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumValueSum([[1,2,3],[4,5,6],[7,8,9]]))  # 15
    print(solution.maximumValueSum([[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]))  # 4
