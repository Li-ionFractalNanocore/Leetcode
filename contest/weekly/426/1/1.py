class Solution:
    def smallestNumber(self, n: int) -> int:
        l = n.bit_length()
        return (1 << l) - 1

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestNumber(5))
    print(solution.smallestNumber(10))
    print(solution.smallestNumber(3))
        