from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        num_counter = [0] * 1002
        result = 0

        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    j_l = arr[j] - a
                    j_r = arr[j] + a
                    k_l = arr[k] - c
                    k_r = arr[k] + c
                    left = max(0, j_l, k_l)
                    right = min(1000, j_r, k_r)
                    if left <= right:
                        result += num_counter[right+1] - num_counter[left]
            for num in range(arr[j], 1001):
                num_counter[num+1] += 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))  # 4