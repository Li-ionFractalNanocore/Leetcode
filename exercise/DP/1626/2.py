from typing import List


# time: 241ms
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(scores, ages))
        max_scores = [0] * 1001
        for i, (score_i, age_i) in enumerate(players):
            max_scores[age_i] = max(max_scores[:age_i+1]) + score_i
        return max(max_scores)


if __name__ == '__main__':
    solution = Solution()
    print(solution.bestTeamScore([4,5,6,5], [2,1,2,1]))  # 16