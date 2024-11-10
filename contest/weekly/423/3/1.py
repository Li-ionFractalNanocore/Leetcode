from typing import List


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        counter = {}
        for num in nums:
            sum_smaller, count_smaller = counter.get(num - 1, (0, 0))
            sum_new = (sum_smaller + num * count_smaller) % MOD
            count_new = count_smaller
            sum_larger, count_larger = counter.get(num + 1, (0, 0))
            sum_new += sum_larger + num * count_larger
            count_new += count_larger
            sum_new += num
            count_new += 1

            num_sum, num_count = counter.get(num, (0, 0))
            counter[num] = ((num_sum + sum_new) % MOD, num_count + count_new)
            result = (result + sum_new) % MOD
        return result % MOD


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOfGoodSubsequences([1, 2, 1]))  # 14
    print(solution.sumOfGoodSubsequences([3, 4, 5]))  # 40
        