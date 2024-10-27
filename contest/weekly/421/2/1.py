class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counter = [0] * 26
        MOD = 10 ** 9 + 7
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for i in range(t):
            z_num = counter[25]
            for j in range(25, 0, -1):
                counter[j] = counter[j - 1]
            counter[0] = z_num
            counter[1] = (counter[1] + z_num) % MOD
        return sum(counter) % MOD

        

        