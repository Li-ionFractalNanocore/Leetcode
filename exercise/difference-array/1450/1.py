from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        l = max(max(endTime), queryTime)
        diff_array = [0] * (l + 2)
        for i in range(len(startTime)):
            diff_array[startTime[i]] += 1
            diff_array[endTime[i] + 1] -= 1
        value = 0
        for i in range(1, queryTime + 1):
            value += diff_array[i]
        return value

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.busyStudent([1,2,3], [3,2,7], 4))  # 1
    print(solution.busyStudent([4], [4], 4))  # 1
    print(solution.busyStudent([4], [4], 5))  # 0
    print(solution.busyStudent([1,1,1,1], [1,3,2,4], 7))  # 0
    print(solution.busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5))  # 5