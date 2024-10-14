from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        l_tree = SortedList()
        l_sum = 0
        r_tree = SortedList()
        counter = defaultdict(int)

        def add(num):
            nonlocal l_sum
            if counter[num] == 0:
                return
            item = (counter[num], num)

            if len(l_tree) == x and item < l_tree[0]:
                r_tree.add(item)
            else:
                l_tree.add(item)
                l_sum += counter[num] * num
                if len(l_tree) > x:
                    l_item = l_tree.pop(0)
                    r_tree.add(l_item)
                    l_sum -= l_item[0] * l_item[1]

        def remove(num):
            nonlocal l_sum
            if counter[num] == 0:
                return
            item = (counter[num], num)

            if item in r_tree:
                r_tree.remove(item)
            else:
                l_tree.remove(item)
                l_sum -= counter[num] * num
                if r_tree:
                    r_item = r_tree.pop(-1)
                    l_tree.add(r_item)
                    l_sum += r_item[0] * r_item[1]

        n = len(nums)
        for i in range(k - 1):
            remove(nums[i])
            counter[nums[i]] += 1
            add(nums[i])

        results = []
        for i in range(k - 1, n):
            remove(nums[i])
            counter[nums[i]] += 1
            add(nums[i])
            results.append(l_sum)
            remove(nums[i - k + 1])
            counter[nums[i - k + 1]] -= 1
            add(nums[i - k + 1])
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.findXSum([1,1,2,2,3,4,2,3], 6, 2))  # [6,10,12]


