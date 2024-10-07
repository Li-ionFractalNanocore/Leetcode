from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        now = bricks
        height = heights[0]
        brick_queue = []
        for i in range(1, n):
            if heights[i] > height:
                heapq.heappush(brick_queue, height - heights[i])
                now -= heights[i] - height
                while brick_queue and now < 0 and ladders > 0:
                    now += -heapq.heappop(brick_queue)
                    ladders -= 1
                if now < 0:
                    return i - 1
            height = heights[i] 
        return n - 1
