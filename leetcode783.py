# 783. 二叉搜索树节点最小距离
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nodes = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        dfs(root)
        ans = float("inf")
        for i in range(len(nodes)-1):
            tmp = abs(nodes[i]-nodes[i+1])
            if tmp<ans:
                ans = tmp
        return ans
        
        