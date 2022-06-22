# 513. 找树左下角的值
# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

# 假设二叉树中至少有一个节点。

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = list()
        queue.append(root)
        ans = queue[0].val
        while queue:
            nextQueue = []
            for q in queue:
                if q.left:
                    nextQueue.append(q.left)
                if q.right:
                    nextQueue.append(q.right)
            queue = nextQueue
            if queue:
                ans=queue[0].val
        return ans