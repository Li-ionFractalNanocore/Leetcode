from collections import defaultdict
from bisect import bisect_right, bisect_left
from typing import List


class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [(0, 0)] * (2 << n.bit_length())
        self.arr = arr
        self.build(1, 0, n - 1)

    def build(self, idx, l, r):
        """
        idx: the index of the tree not the index of the array
        """
        if l == r:
            self.tree[idx] = (self.arr[l], 1)
            return
        m = (l + r) // 2
        self.build(idx * 2, l, m)
        self.build(idx * 2 + 1, m + 1, r)
        self.tree[idx] = self.merge(self.tree[idx * 2], self.tree[idx * 2 + 1])


    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a[0] == b[0]:
            return (a[0], a[1] + b[1])
        elif a[1] >= b[1]:
            return (a[0], a[1] - b[1])
        else:
            return (b[0], b[1] - a[1])

    def query(self, idx, l, r, ql, qr):

        if l > qr or r < ql:
            return None

        if ql <= l and r <= qr:
            return self.tree[idx]

        m = (l + r) // 2
        l_r = self.query(idx * 2, l, m, ql, qr)
        r_r = self.query(idx * 2 + 1, m + 1, r, ql, qr)
        return self.merge(l_r, r_r)


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.num_indices = defaultdict(list)
        for i, num in enumerate(arr):
            self.num_indices[num].append(i)
        self.st = SegmentTree(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        res = self.st.query(1, 0, len(self.st.arr) - 1, left, right)
        cnt = bisect_right(self.num_indices[res[0]], right) - bisect_left(self.num_indices[res[0]], left)
        return res[0] if cnt >= threshold else -1
        

if __name__ == '__main__':
    solution = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(solution.query(0, 5, 4))
    print(solution.query(0, 3, 3))
    print(solution.query(2, 3, 2))