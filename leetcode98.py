# 98. 验证二叉搜索树

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nums = []
        def inOrder(tree):
            if tree is None:
                return
            inOrder(tree.left)
            nums.append(tree.val)
            inOrder(tree.right)
        inOrder(root)
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                return False
        return True

