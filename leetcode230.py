# 230. 二叉搜索树中第K小的元素
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        count=0
        
        def midOrder(node):
            nonlocal res
            nonlocal count
            if not node:
                return
            midOrder(node.left)
            count+=1
            if count==k:
                res=node.val
                return
            midOrder(node.right)
        midOrder(root)
        return res

import TreeNodeUtil

sol = Solution()
root = [3,1,4,None,2]
k = 1
tree = TreeNodeUtil.createTreeFromList(root)
print(sol.kthSmallest(tree,k))