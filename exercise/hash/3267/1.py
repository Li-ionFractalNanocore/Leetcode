from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        powers = [10 ** i for i in range(10)]
        result = 0
        nums.sort()
        counter = defaultdict(int)
        for num in nums:
            num_changed = {num}
            num_list = list(map(int, str(num)))
            num_list.reverse()
            n = len(num_list)
            for i in range(n):
                for j in range(i + 1, n):
                    if num_list[i] == num_list[j]:
                        continue
                    new_num = num + (int(num_list[i]) - int(num_list[j])) * (powers[j] - powers[i])
                    num_changed.add(new_num)
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    for k in range(i + 1, n):
                        for l in range(k + 1, n):
                            if num_list[k] == num_list[l]:
                                continue
                            new_new_num = new_num + (int(num_list[k]) - int(num_list[l])) * (powers[l] - powers[k])
                            num_changed.add(new_new_num)
            result += sum(counter[m] for m in num_changed)
            counter[num] += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPairs([1023,2310,2130,213])) # 4