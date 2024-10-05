from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sorted_rating = sorted(rating)
        mapping = {x: i + 1 for i, x in enumerate(sorted_rating)}
        n = len(rating)
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
        for i, rate in enumerate(rating):
            index = mapping[rate]
            smaller_before = search(index - 1)
            update(index)
            larger_before = i - smaller_before
            smaller_after = index - smaller_before - 1
            larger_after = n - i - 1 - smaller_after
            result += smaller_before * larger_after + larger_before * smaller_after
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numTeams([2,5,3,4,1]))  # 3