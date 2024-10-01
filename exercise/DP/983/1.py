from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        days_cost = [float('inf')] * 366
        last_day = 0
        days_cost[0] = 0
        for i in range(n):
            day = days[i]
            for j in range(30):
                if day+j > 365:
                    break
                if j < 1:
                    days_cost[day+j] = min(days_cost[day+j], days_cost[last_day] + costs[0])
                if j < 7:
                    days_cost[day+j] = min(days_cost[day+j], days_cost[last_day] + costs[1])
                if j < 30:
                    days_cost[day+j] = min(days_cost[day+j], days_cost[last_day] + costs[2])
            last_day = day
        return days_cost[days[-1]]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.mincostTickets([1,4,6,7,8,20], [2,7,15]))  # 11
            