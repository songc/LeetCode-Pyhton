# 102. 二叉树的层序遍历
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        tmp = []
        if root:
            tmp.append(root)
        while tmp:
            v = []
            nodes = []
            for node in tmp:
                if node:
                    v.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            tmp = nodes
            ans.append(v)
        return ans