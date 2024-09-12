from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        l = 0
        pre_max = [0] * (n + 1)
        result = 0
        for r, num in enumerate(prizePositions):
            while prizePositions[l] < num - k:
                l += 1
            result = max(result, r - l + 1 + pre_max[l])
            pre_max[r+1] = max(pre_max[r], r - l + 1)
        return result
            

if __name__ == '__main__':
    solution = Solution()
    print(solution.maximizeWin([1,1,2,2,3,3,5], 2))  # 7
    print(solution.maximizeWin([1,2,3,4], 0))  # 2