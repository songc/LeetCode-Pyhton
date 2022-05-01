# 1305. 两棵二叉搜索树中的所有元素
# 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

from typing import List



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        def preOrd(node):
            if node:
                yield from preOrd(node.left)
                yield node.val
                yield from preOrd(node.right)
        g1 = preOrd(root1)
        g2 = preOrd(root2)
        v1 = next(g1,None)
        v2 = next(g2,None)
        while v1 is not None  or v2 is not None:
            if v1 is None:
                ans.append(v2)
                v2=next(g2,None)
                continue
            if v2 is None:
                ans.append(v1)
                v1 = next(g1,None)
                continue
            if v1<=v2:
                ans.append(v1)
                v1=next(g1,None)
            else:
                ans.append(v2)
                v2 = next(g2,None)
        return ans


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        def preOrd(node):
            if node is None:
                return
            preOrd(node.left)
            ans.append(node.val)
            preOrd(node.right)
        preOrd(root1)
        preOrd(root2)
        ans.sort()
        return ans
