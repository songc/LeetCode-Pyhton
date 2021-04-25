# 94. 二叉树的中序遍历
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def inOrder(tree):
            if tree.left:
                inOrder(tree.left)
            ans.append(tree.val)
            if tree.right:
                inOrder(tree.right)
        if root:
            inOrder(root)
        return ans

class Solution2:
    def inorderTraversal(self, root: TreeNode)-> List[int]:
        ans = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
                continue
            node = stack.pop()
            ans.append(node.val)
            root=node.right
        return ans
        