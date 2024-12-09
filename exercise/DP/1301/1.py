from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        dp1 = [0] * n
        dp2 = [0] * n

        dp2[-1] = 1
        for i in range(n - 2, -1, -1):
            if board[-1][i] == 'X' or dp1[i+1] == -1:
                dp1[i] = -1
                dp2[i] = 0
            else:
                dp1[i] = dp1[i+1] + int(board[-1][i])
                dp2[i] = 1                
        
        for i in range(m - 2, -1, -1):
            new_dp1 = [0] * n
            new_dp2 = [0] * n
            if board[i][n - 1] == 'X' or dp1[n - 1] == -1:
                new_dp1[n - 1] = -1
                new_dp2[n - 1] = 0
            else:
                new_dp1[n - 1] = dp1[n-1] + int(board[i][n - 1])
                new_dp2[n - 1] = 1
            for j in range(n - 2, -1, -1):
                if board[i][j] == 'X':
                    new_dp1[j] = -1
                    new_dp2[j] = 0
                else:
                    new_dp = max(dp1[j+1], dp1[j], new_dp1[j+1])
                    if new_dp == -1:
                        new_dp1[j] = -1
                        new_dp2[j] = 0
                        continue
                    new_dp1[j] = new_dp + (int(board[i][j]) if board[i][j] != 'E' else 0)
                    if new_dp == new_dp1[j+1]:
                        new_dp2[j] += new_dp2[j+1]
                    if new_dp == dp1[j]:
                        new_dp2[j] += dp2[j]
                    if new_dp == dp1[j+1]:
                        new_dp2[j] += dp2[j+1]
                    new_dp2[j] %= 10**9 + 7
            dp1, dp2 = new_dp1, new_dp2
        return [dp1[0], dp2[0]] if dp1[0] != -1 else [0, 0]

            
if __name__ == '__main__':
    solution = Solution()
    print(solution.pathsWithMaxScore(["E11345","X452XX","3X43X4","44X312","2345XX","1342XS"]))
    print(solution.pathsWithMaxScore(["E23","2X2","12S"]))  # [7, 1]
        