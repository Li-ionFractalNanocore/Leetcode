from typing import List
from collections import defaultdict


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = [0] * 51
        result = []

        for i in range(k - 1):
            counter[nums[i]] += 1

        for i in range(k - 1, len(nums)):
            counter[nums[i]] += 1
            num_counter = defaultdict(list)
            for j in range(50, 0, -1):
                num_counter[counter[j]].append(j)
            c = 0
            res = 0
            for j in range(50, 0, -1):
                if num_counter[j]:
                    for num in num_counter[j]:
                        res += num * j
                        c += 1
                        if c == x:
                            break
                if c == x:
                    break
            counter[nums[i - k + 1]] -= 1
            result.append(res)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)) # [4,7,6]

