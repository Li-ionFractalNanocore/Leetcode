from typing import List
import heapq


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []

        def distance(x, y):
            return abs(x) + abs(y)
        
        results = []
        for x, y in queries:
            dis = -distance(x, y)
            if len(heap) == k and dis > heap[0]:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, dis)
            if len(heap) == k:
                results.append(-heap[0])
            else:
                results.append(-1)
        
        return results
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.resultsArray([[1,2],[3,4],[2,3],[-3,0]], 2))  # [-1,7,5,3]
    print(solution.resultsArray([[5,5],[4,4],[3,3]], 1))  # [10,8,6]
        
        