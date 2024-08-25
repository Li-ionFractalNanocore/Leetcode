from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)

        def check(a, b):
            str_a = str(a)
            if len(str_a) < 7:
                str_a = "0" * (7 - len(str_a)) + str_a
            str_b = str(b)
            if len(str_b) < 7:
                str_b = "0" * (7 - len(str_b)) + str_b
            if str_a == str_b:
                return True
            diff_c = []
            for i in range(7):
                if str_a[i] != str_b[i]:
                    diff_c.append(i)
                    if len(diff_c) > 2:
                        return False
            if len(diff_c) < 2:
                return False
            if str_a[diff_c[0]] == str_b[diff_c[1]] and str_a[diff_c[1]] == str_b[diff_c[0]]:
                return True

        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if check(nums[i], nums[j]):
                    result += 1
        return result
        


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPairs([3,12,30,17,21]))  # 2
    print(solution.countPairs([1,1,1,1,1]))  # 10
    print(solution.countPairs([1,2,3,4,5]))  # 0

