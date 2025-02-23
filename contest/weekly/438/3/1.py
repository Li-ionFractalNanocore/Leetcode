import math


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        digits = [int(c) for c in s]

        def gen_triangle(n):
            comb_mod5 = [
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 2, 1, 0, 0],
                [1, 3, 3, 1, 0],
                [1, 4, 1, 4, 1],
            ]
            
            n_base5_low = []
            temp = n
            while temp > 0:
                n_base5_low.append(temp % 5)
                temp = temp // 5
            
            row = []
            for k in range(n + 1):
                a = 1 if (k & n) == k else 0
                
                remaining = k
                product = 1
                valid = True
                for i in range(len(n_base5_low)):
                    if remaining == 0:
                        break
                    k_i = remaining % 5
                    d_i = n_base5_low[i]
                    if k_i > d_i:
                        valid = False
                        break
                    product = (product * comb_mod5[d_i][k_i]) % 5
                    remaining = remaining // 5
                if remaining > 0:
                    valid = False
                b = product % 5 if valid else 0
                
                x = (5 * a + 6 * b) % 10
                row.append(x)
            
            return row

        line_n = gen_triangle(n - 2)
        a = sum([line_n[i] * digits[i] % 10 for i in range(n - 1)]) % 10
        b = sum([line_n[i - 1] * digits[i] % 10 for i in range(1, n)]) % 10

        return a == b
            

if __name__ == '__main__':
    solution = Solution()
    print(solution.hasSameDigits("3902"))
    print(solution.hasSameDigits("34789"))
    print(solution.hasSameDigits("1" * 10**5))
