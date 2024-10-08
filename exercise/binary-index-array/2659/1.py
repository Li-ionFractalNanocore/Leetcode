from typing import List


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums_tuple = [(index, num) for index, num in enumerate(nums)]
        nums_tuple.sort(key=lambda x: x[1])
        pre = 0
        deleted = [0] * (n + 1)

        def update(x):
            while x <= n:
                deleted[x] += 1
                x += x & -x

        def search(x):
            result = 0
            while x:
                result += deleted[x]
                x -= x & -x
            return result

        result = n
        for index, num in nums_tuple:
            if index >= pre:
                result += index - pre - search(index) + search(pre)
            else:
                result += n - pre + index - 1 - (search(n) - search(pre + 1) + search(index))
            pre = index
            update(index + 1)
        
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countOperationsToEmptyArray([1,2,4,3]))  # 5
    print(solution.countOperationsToEmptyArray([3,4,-1]))  # 5