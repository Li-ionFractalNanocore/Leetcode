class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        pos = [[] for _ in range(10)]

        # from right to left, so we can pop digit most left
        for i in range(n - 1, -1, -1):
            pos[int(num[i])].append(i)

        remove_counter = [0] * (n + 1)
        def update(index: int) -> None:
            while index < len(remove_counter):
                remove_counter[index] += 1
                index += index & -index

        def query(index: int) -> int:
            result = 0
            while index > 0:
                result += remove_counter[index]
                index -= index & -index
            return result

        result = ""
        for i in range(n):
            for j in range(10):
                if pos[j]:
                    move = query(n) - query(pos[j][-1])
                    real_pos = pos[j][-1] + move - i
                    if real_pos <= k:
                        update(pos[j][-1] + 1)
                        pos[j].pop()
                        result += str(j)
                        k -= real_pos
                        break

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minInteger(num = "4321", k = 4)) # "1342"
        
