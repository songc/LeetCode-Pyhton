# 653. 两数之和 IV - 输入 BST
# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vset=set()
        def preOrder(node):
            if not node:
                return False
            if k-node.val in vset:
                return True
            vset.add(node.val)
            return preOrder(node.left) or preOrder(node.right)
        
        return preOrder(root)