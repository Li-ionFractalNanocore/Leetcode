from math import isqrt


is_primes = [0] * 100001
for i in range(2, 100001):
    if is_primes[i] == 0:
        is_primes[i] = is_primes[i - 1] + 1
        for j in range(i * i, 100000, i):
            is_primes[j] = -1
    else:
        is_primes[i] = is_primes[i - 1]

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        return r - l + 1 - is_primes[isqrt(r)] + is_primes[isqrt(l - 1)]

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.nonSpecialCount(4, 16))
    print(solution.nonSpecialCount(5, 7))
        