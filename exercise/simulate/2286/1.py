from typing import List


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.mins = [0] * (2 * (1 << n.bit_length()))
        self.sums = [0] * (2 * (1 << n.bit_length()))

    def update(self, o, l, r, idx, val):
        if l == r:
            self.mins[o] += val
            self.sums[o] += val
            return
        m = (l + r) // 2
        if idx <= m:
            self.update(o * 2, l, m, idx, val)
        else:
            self.update(o * 2 + 1, m + 1, r, idx, val)
        self.mins[o] = min(self.mins[o * 2], self.mins[o * 2 + 1])
        self.sums[o] = self.sums[o * 2] + self.sums[o * 2 + 1]

    def search_min(self, o, l, r, r_range, val):
        if self.mins[o] > self.m - val:
            return -1
        if l == r:
            return l
        m = (l + r) // 2
        if self.mins[o * 2] <= self.m - val:
            return self.search_min(o * 2, l, m, r_range, val)
        if r_range > m and self.mins[o * 2 + 1] <= self.m - val:
            return self.search_min(o * 2 + 1, m + 1, r, r_range, val)
        return -1

    def query_sum(self, o, l, r, l_range, r_range):
        if l_range <= l and r <= r_range:
            return self.sums[o]
        m = (l + r) // 2
        result = 0
        if l_range <= m:
            result += self.query_sum(o * 2, l, m, l_range, r_range)
        if r_range > m:
            result += self.query_sum(o * 2 + 1, m + 1, r, l_range, r_range)
        return result

    def gather(self, k: int, maxRow: int) -> List[int]:
        index = self.search_min(1, 0, self.n - 1, maxRow, k)
        if index == -1:
            return []
        c = self.query_sum(1, 0, self.n - 1, index, index)
        self.update(1, 0, self.n - 1, index, k)
        return [index, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        sum_ = self.query_sum(1, 0, self.n - 1, 0, maxRow)
        if sum_ > self.m * (maxRow + 1) - k:
            return False
        first = self.search_min(1, 0, self.n - 1, maxRow, 1)
        while k:
            now = self.query_sum(1, 0, self.n - 1, first, first)
            use = min(k, self.m - now)
            k -= use
            self.update(1, 0, self.n - 1, first, use)
            first += 1
        return True



# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)


if __name__ == '__main__':
    solution = BookMyShow(2, 5)
    print(solution.gather(4, 0))
    print(solution.gather(2, 0))
    print(solution.scatter(5, 1))
    print(solution.scatter(5, 1))
    