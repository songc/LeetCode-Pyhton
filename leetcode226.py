# 226. 翻转二叉树
# 翻转一棵二叉树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left,root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right) 