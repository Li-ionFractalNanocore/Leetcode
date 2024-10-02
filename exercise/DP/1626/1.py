from typing import List


# time: 883ms
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(scores, ages))
        score_sum = [0] * n
        res = 0
        for i, (score_i, age_i) in enumerate(players):
            for j in range(i):
                if players[j][1] <= age_i:
                    score_sum[i] = max(score_sum[i], score_sum[j])
            score_sum[i] += score_i
            res = max(res, score_sum[i])
        return res

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.bestTeamScore([4,5,6,5], [2,1,2,1]))  # 16
            