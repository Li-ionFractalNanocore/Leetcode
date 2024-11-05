class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        round = min(x, y // 4)
        if round & 1:
            return "Alice"
        else:
            return "Bob"