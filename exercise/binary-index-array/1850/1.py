from collections import defaultdict


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num_list = list(num)
        n = len(num_list)
        for i in range(k):
            stack = []
            for j in range(n - 1, -1, -1):
                if not stack or num_list[j] >= stack[-1][0]:
                    stack.append((num_list[j], j))
                else:
                    last = stack.pop()
                    while stack and num_list[j] < stack[-1][0]:
                        last = stack.pop()
                    num_list[last[1]] = num_list[j]
                    num_list[j] = last[0]
                    for k in range((n - j - 1) // 2):
                        num_list[j + 1 + k], num_list[n - 1 - k] = num_list[n - 1 - k], num_list[j + 1 + k]
                    break
        
        c_index = defaultdict(list)
        for i in range(n - 1, -1, -1):
            c_index[num[i]].append(i)
        for i in range(n):
            num_list[i] = c_index[num_list[i]].pop()

        bit = [0] * (n + 1)

        def update(index):
            while index <= n:
                bit[index] += 1
                index += index & -index

        def query(index):
            result = 0
            while index:
                result += bit[index]
                index -= index & -index
            return result

        result = 0
        for i in range(n):
            result += i - query(num_list[i] + 1)
            update(num_list[i] + 1)
        return result
        

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.getMinSwaps("5489355142", 4)) # 2