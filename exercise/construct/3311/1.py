from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        degree = [0] * n
        graph = [[] for _ in range(n)]
        for from_, to_ in edges:
            degree[from_] += 1
            degree[to_] += 1
            graph[from_].append(to_)
            graph[to_].append(from_)

        degree_counter = {1: [], 2: [], 3: [], 4: []}
        for i in range(n):
            degree_counter[degree[i]].append(i)

        rows = []
        row = []
        visited = [False] * n
        if degree_counter[1]:
            row.append(degree_counter[1][0])
            visited[degree_counter[1][0]] = True
        else:
            row.append(degree_counter[2][0])
            now = degree_counter[2][0]
            visited[now] = True
            while True:
                next_ = -1
                for next_choise in graph[now]:
                    if visited[next_choise]:
                        continue
                    if degree[next_choise] == 2:
                        next_ = next_choise
                        break
                    if degree[next_choise] == 3:
                        next_ = next_choise
                row.append(next_)
                visited[next_] = True
                if degree[next_] == 2:
                    break
                now = next_
        rows.append(row)

        for r_index in range(1, n // len(row)):
            row = []
            for i in range(len(rows[0])):
                for next_choise in graph[rows[-1][i]]:
                    if visited[next_choise]:
                        continue
                    row.append(next_choise)
                    visited[next_choise] = True
                    break
            rows.append(row)
        return rows


if __name__ == '__main__':
    solution = Solution()
    print(solution.constructGridLayout(n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]])) # [[8,6,3],[7,4,2],[1,0,5]]
    print(solution.constructGridLayout(n = 6, edges = [[0,1],[1,2],[2,3],[3,0],[3,4],[4,5],[2,5]])) # [[0,1],[3,2],[4,5]]
    print(solution.constructGridLayout(n = 4, edges = [[0,1],[1,2],[2,3],[3,0]])) # [[0,1],[3,2]]




