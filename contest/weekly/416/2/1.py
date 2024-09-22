from typing import List
import heapq


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        worker_queue = []
        for worker in workerTimes:
            heapq.heappush(worker_queue, (worker, 1))

        res = 0
        for i in range(mountainHeight):
            worker, count = heapq.heappop(worker_queue)
            res = max(res, worker)
            item = worker // ((1 + count) * count // 2)
            heapq.heappush(worker_queue, (item * (count + 2) * (count + 1) // 2, count + 1))
        
        return res

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.minNumberOfSeconds(4, [2, 1, 1]))  # 3
    print(solution.minNumberOfSeconds(10, [3,2,2,4]))  # 12
    print(solution.minNumberOfSeconds(5, [1]))  # 15

