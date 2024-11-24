from collections import defaultdict


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)
        dis = len(s) // k
        for i in range(0, len(s), dis):
            counter_s[s[i:i + dis]] += 1
        for i in range(0, len(t), dis):
            counter_t[t[i:i + dis]] += 1
        if len(counter_s) != len(counter_t):
            return False
        for key in counter_s:
            if counter_s[key] != counter_t[key]:
                return False
        return True

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.isPossibleToRearrange('abcd', 'cdab', 2))  # True
    print(solution.isPossibleToRearrange('aabbcc', 'bbaacc', 3))  # True
    print(solution.isPossibleToRearrange('aabbcc', 'bbaacc', 2))  # False
        