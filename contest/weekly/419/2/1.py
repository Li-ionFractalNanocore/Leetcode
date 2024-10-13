from typing import Optional
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        res_queue = []

        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == right and left >= 0:
                res = left + right + 1
                heapq.heappush(res_queue, res)
                return res
            else:
                return -1

        dfs(root)
        n = len(res_queue)
        if k > n:
            return -1

        for i in range(n - k):
            heapq.heappop(res_queue)
        
        return res_queue[0]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(solution.kthLargestPerfectSubtree(root, 1)) # 7
        