from typing import List


class Solution:
    def reversePairs(self, record: List[int]) -> int:
        n = len(record)
        record_sorted = sorted(record)
        record_mapping = {record_sorted[i]: i + 1 for i in range(n)}

        bit = [0] * (n + 1)
        def update(x):
            while x <= n:
                bit[x] += 1
                x += x & -x
        
        def search(x):
            res = 0
            while x > 0:
                res += bit[x]
                x -= x & -x
            return res
        
        ans = 0
        for i in range(n):
            ans += i - search(record_mapping[record[i]])
            update(record_mapping[record[i]])

        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.reversePairs([2, 4, 3, 5, 1])) # 5