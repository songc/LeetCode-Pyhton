# 897. 递增顺序搜索树
# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def midRe(node):
            if node is None:
                return
            midRe(node.left)
            ans.append(node)
            midRe(node.right)
        midRe(root)
        for i in range(1,len(ans)):
            ans[i-1].right=ans[i]
            ans[i].left=None
        return ans[0]

class Solution2:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        pre = dummy
        def midRe(node):
            nonlocal pre
            if node is None:
                return
            midRe(node.left)
            pre.right = node
            pre = pre.right
            node.left= None
            midRe(node.right)
        midRe(root)
        return dummy.right
