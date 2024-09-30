class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        counter = {'W': 0, 'B': 0}
        for i in range(k):
            counter[blocks[i]] += 1
        result = counter['W']

        for i in range(k, n):
            counter[blocks[i]] += 1
            counter[blocks[i - k]] -= 1
            result = min(result, counter['W'])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumRecolors("WBBWWBBWBW", 7))  # 3
