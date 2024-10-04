from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        mapping = {x: i for i, x in enumerate(nums2)}
        for i in range(n):
            nums1[i] = mapping[nums1[i]]

        counter = [0] * (n + 1)

        def update(x):
            while x <= n:
                counter[x] += 1
                x += x & -x
        
        def search(x):
            res = 0
            while x:
                res += counter[x]
                x -= x & -x
            return res

        result = 0
        update(nums1[0] + 1)
        for i in range(1, n - 1):
            smaller_count = search(nums1[i])
            larger_count = (n - i - 1) - (nums1[i] - smaller_count)
            result += smaller_count * larger_count
            update(nums1[i] + 1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.goodTriplets([2,0,1,3], [0,1,2,3]))  # 1
