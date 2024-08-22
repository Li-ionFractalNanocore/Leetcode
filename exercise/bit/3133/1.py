class Solution:
    def minEnd(self, n: int, x: int) -> int:

        def to_list(num):
            result = []
            while num:
                result.append(num & 1)
                num >>= 1
            return result
        
        n_list = to_list(n - 1)
        x_list = to_list(x)
        i = 0
        for j in range(len(n_list)):
            while i < len(x_list) and x_list[i] == 1:
                i += 1
            if i == len(x_list):
                x_list.append(n_list[j])
            else:
                x_list[i] = n_list[j]
            i += 1
        return sum([x_list[i] * (1 << i) for i in range(len(x_list))])


solution = Solution()
print(solution.minEnd(3, 4)) # 6
print(solution.minEnd(2, 7)) # 15
        
        