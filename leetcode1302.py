# 1302. 层数最深叶子节点的和
# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans=root.val
        queue  = [root]
        while queue:
            tmp = 0
            nextQueue = []
            for n in queue:
                tmp+=n.val
                if n.left:
                    nextQueue.append(n.left)
                if n.right:
                    nextQueue.append(n.right)
            ans = tmp
            queue = nextQueue
        return ans
                