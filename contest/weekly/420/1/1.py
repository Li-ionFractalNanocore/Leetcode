from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        results = []
        word = ''
        now = ord('a')
        for i in range(len(target)):
            while chr(now) != target[i]:
                results.append(word + chr(now))
                now += 1
            word += chr(now)
            results.append(word)
            now = ord('a')
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.stringSequence('abc')) # ['a', 'aa', 'ab', 'aba', 'abb', 'abc']

        