from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        r = -1
        counter = defaultdict(int)
        double_counter = 0
        result = 0
        for l in range(n):
            while r + 1 < n and double_counter < 1:
                r += 1
                counter[s[r]] += 1
                if counter[s[r]] == k:
                    double_counter += 1
            if double_counter < 1:
                break
            result += n - r
            counter[s[l]] -= 1
            if counter[s[l]] == k - 1:
                double_counter -= 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfSubstrings("abacb", 2)) # 4
    print(solution.numberOfSubstrings("abcde", 1)) # 15
                
        