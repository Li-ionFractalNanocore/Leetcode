from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        num = 0
        for command in commands:
            if command == "UP":
                num -= n
            elif command == "DOWN":
                num += n
            elif command == "LEFT":
                num -= 1
            else:
                num += 1
        return num