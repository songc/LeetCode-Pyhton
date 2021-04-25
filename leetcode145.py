# 145. 二叉树的后序遍历
# 给定一个二叉树，返回它的 后序 遍历。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        pre = None
        stack = []
        while stack or root:
            while root:
                stack.append(root.left)
                root = root.left
            root = stack.pop()
            if not root.right or root.right==pre:
                ans.append(root.val)
                pre = root
                root = None
            else:
                stack.append(root)
                root=root.right
        return ans