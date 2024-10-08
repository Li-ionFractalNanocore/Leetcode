from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        one_set = set([path[1] for path in paths])
        for path in paths:
            if path[0] in one_set:
                one_set.remove(path[0])
        return one_set.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # "Sao Paulo"