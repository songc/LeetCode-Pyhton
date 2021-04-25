# 144. 二叉树的前序遍历
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            if root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
                continue
            node = stack.pop()
            root=node.right
        return ans