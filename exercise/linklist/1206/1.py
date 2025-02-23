import random

MAX_LEVEL = 10

class Node:
    def __init__(self, val):
        self.val = val
        self.next = [None] * MAX_LEVEL


class Skiplist:

    def __init__(self):
        self.head = Node(-1)

    def find(self, target: int):
        update = [None] * MAX_LEVEL
        cur = self.head
        for i in range(MAX_LEVEL - 1, -1, -1):
            while cur.next[i] and cur.next[i].val < target:
                cur = cur.next[i]
            update[i] = cur
        return update

    def search(self, target: int) -> bool:
        update = self.find(target)
        return update[0].next[0] is not None and update[0].next[0].val == target

    def add(self, num: int) -> None:
        update = self.find(num)
        new_node = Node(num)
        for i in range(MAX_LEVEL):
            update[i].next[i], new_node.next[i] = new_node, update[i].next[i]
            if random.randint(0, 1):
                break

    def erase(self, num: int) -> bool:
        update = self.find(num)
        node = update[0].next[0]
        if not node or node.val != num:
            return False
        for i in range(MAX_LEVEL):
            if update[i].next[i] == node:
                update[i].next[i] = update[i].next[i].next[i]
        return True
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)