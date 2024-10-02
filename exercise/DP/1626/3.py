
from typing import List


# time: 99ms
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(scores, ages))
        max_scores = [0] * 1001

        def update(i, score):
            while i < 1001:
                max_scores[i] = max(max_scores[i], score)
                i += i & -i

        def search(i):
            res = 0
            while i:
                res = max(res, max_scores[i])
                i -= i & -i
            return res

        for score, age in players:
            new_score = search(age) + score
            update(age, new_score)
        
        return max(max_scores)
            


if __name__ == '__main__':
    solution = Solution()
    print(solution.bestTeamScore([4,5,6,5], [2,1,2,1]))  # 16