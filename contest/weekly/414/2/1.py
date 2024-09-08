from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        first, last = start[0], start[-1] + d
        n = len(start)

        def check(dis):
            now = first
            for i in range(1, n):
                if start[i] - now > dis:
                    now = start[i]
                elif start[i] + d - now < dis:
                    return False
                else:
                    now = now + dis
            return True
        
        l, r = 0, (last - first) // (n - 1)
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPossibleScore([2, 9, 13, 13], 5))  # 4
    print(solution.maxPossibleScore([2, 6, 13, 13], 5))  # 5
    print(solution.maxPossibleScore([6, 0, 3], 2))  # 4
                
                
                    