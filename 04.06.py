# 面试题 04.06. 后继者
# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

# 如果指定节点没有对应的“下一个”节点，则返回null。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pre = None
        def inOrder(node):
            nonlocal pre
            if node:
                ans = inOrder(node.left)
                if ans:
                    return ans
                if pre==p:
                    return node
                pre = node
                return inOrder(node.right)
        return inOrder(root)

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pre = None
        ans = None
        def inOrder(node):
            nonlocal pre, ans
            if node:
                inOrder(node.left)
                if pre==p and ans is None:
                    ans = node
                    return
                pre = node
                inOrder(node.right)
        inOrder(root)
        return ans

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None
        if p.right:
            ans=p.right
            while ans.left:
                ans= ans.left
            return ans
        node = root
        while node:
            if node.val>p:
                ans = node
                node = node.left
            else:
                node = node.right
        return ans
