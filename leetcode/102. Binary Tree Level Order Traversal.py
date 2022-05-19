from collections import deque
from typing import *
# Definition for a binary tree node.
root = [3,9,20,None,None,15,7]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_deque = deque([root])
        res=[]
        while node_deque:
            cur_level, size = [], len(node_deque)
            for i in range(size):
                node = node_deque.popleft()
                if node.left:
                    node_deque.append(node.left)
                if node.right:
                    node_deque.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

sol = Solution()

print(sol.levelOrder(root))






