# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。

# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))