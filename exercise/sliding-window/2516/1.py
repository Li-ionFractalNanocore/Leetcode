class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        counter = {'a': 0, 'b': 0, 'c': 0}
        for i in range(n):
            counter[s[i]] += 1
        for key, v in counter.items():
            if v < k:
                return -1
        
        result = n
        full = 3
        r = 0
        for l in range(n):
            while r < n and full == 3:
                if counter[s[r]] > k:
                    counter[s[r]] -= 1
                    r += 1
                else:
                    break
            result = min(result, l + n - r)
            counter[s[l]] += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.takeCharacters("aabaaaacaabc", 2))  # 8


