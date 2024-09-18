from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()
        j = 0
        for bus in buses:
            count = 0
            while j < len(passengers) and count < capacity and passengers[j] <= bus:
                j += 1
                count += 1

        j -= 1
        if count < capacity:
            result = bus
        else:
            result = passengers[j]
        while j >= 0 and passengers[j] == result:
            j -= 1
            result -= 1
        return result
        

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.latestTimeCatchTheBus([10,20], [2,17,18,19], 2)) # 16