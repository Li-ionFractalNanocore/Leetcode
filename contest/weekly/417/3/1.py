class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        r = 0
        aeiou = {'a', 'e', 'i', 'o', 'u'}
        counter = {'p': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        full = 0 if k > 0 else 1
        result = 0
        accm = [0] * n
        now = 1
        for i in range(n - 1, -1, -1):
            accm[i] = now
            if word[i] not in aeiou:
                now = 1
            else:
                now += 1
        for l in range(n):
            while r < n and full < 6 and counter['p'] + int(word[r] not in aeiou) <= k:
                if word[r] in aeiou:
                    counter[word[r]] += 1
                    if counter[word[r]] == 1:
                        full += 1
                else:
                    counter['p'] += 1
                    if counter['p'] == k:
                        full += 1
                r += 1
            if full == 6:
                result += accm[r - 1]
            if word[l] in aeiou:
                counter[word[l]] -= 1
                if counter[word[l]] == 0:
                    full -= 1
            else:
                counter['p'] -= 1
                if counter['p'] == k - 1:
                    full -= 1
        return result

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.countOfSubstrings("ieaouqqieaouqq", 1))
    print(solution.countOfSubstrings("aeiou", 0))
    print(solution.countOfSubstrings("aeioqq", 1))
                