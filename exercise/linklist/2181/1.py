from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        now = result
        first = head
        accum = 0
        while first.next:
            second = first.next
            while second.val != 0:
                accum += second.val
                second = second.next
            now.next = ListNode(accum)
            accum = 0
            now = now.next
            first = second
        return result.next
