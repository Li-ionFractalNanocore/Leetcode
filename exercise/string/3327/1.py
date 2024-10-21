from typing import List


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(s)
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)

        index = [[-1, -1] for _ in range(n)]
        timestamp = 0
        dfs_str = [''] * n

        def dfs(node):
            nonlocal timestamp
            index[node][0] = timestamp
            for next_ in graph[node]:
                dfs(next_)
                timestamp += 1
            index[node][1] = timestamp
            dfs_str[timestamp] = s[node]

        dfs(0)
        extend_s = '^'
        for c in dfs_str:
            extend_s += '#' + c
        extend_s += '#$'

        edge_r = 0
        now_center = 0
        extend_n = len(extend_s)
        s_r = [1] * extend_n
        for i in range(1, extend_n - 1):
            if i <= edge_r:
                s_r[i] = min(s_r[2 * now_center - i], edge_r - i + 1)
            while extend_s[i - s_r[i]] == extend_s[i + s_r[i]]:
                s_r[i] += 1
                edge_r = i + s_r[i] - 1
                now_center = i

        result = []
        for i in range(n):
            l, r = index[i]
            result.append(s_r[l + r + 2] >= r - l + 1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnswer([-1,0,0,1,1,2], 'aababa'))