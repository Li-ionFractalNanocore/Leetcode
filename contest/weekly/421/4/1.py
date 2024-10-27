from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        matrix = [[0] * 26 for _ in range(26)]
        MOD = 10 ** 9 + 7
        for i, num in enumerate(nums):
            for j in range(i + 1, i + num + 1):
                matrix[i][j % 26] += 1

        def multiply(matrix1, matrix2):
            result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += matrix1[i][k] * matrix2[k][j]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    result[i][j] %= MOD
            return result

        def power(matrix, times):
            if times == 1:
                return matrix
            if times & 1:
                return multiply(power(multiply(matrix, matrix), times // 2), matrix)
            return power(multiply(matrix, matrix), times // 2)

        vector = [[0] * 26]
        for c in s:
            vector[0][ord(c) - ord('a')] += 1
        result = multiply(vector, power(matrix, t))
        result = sum(sum(row) for row in result) % MOD
        return result
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthAfterTransformations("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
    print(solution.lengthAfterTransformations("abcyy", 4, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
    print(solution.lengthAfterTransformations("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
    print(solution.lengthAfterTransformations("azbk", 2, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
        