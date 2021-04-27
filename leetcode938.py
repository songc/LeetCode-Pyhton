# 938. 二叉搜索树的范围和
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack=[]
        ans = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
                continue
            root = stack.pop()
            if root.val>high:
                return ans
            if root.val>=low:
                ans+=root.val
            root=root.right
        return ans

class Solution2:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val>high:
            return self.rangeSumBST(root.left,low,high)
        if root.val<low:
            return self.rangeSumBST(root.right,low,high)
        return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
