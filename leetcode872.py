# 872. 叶子相似的树
# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
# 举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
# 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
# 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/leaf-similar-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1=[]
        leaf2=[]
        def midOrder(root,leaf):
            if root.left:
                midOrder(root.left,leaf)
            if not root.left and not root.right:
                leaf.append(root.val)
            if root.right:
                midOrder(root.right,leaf)
        midOrder(root1,leaf1)
        midOrder(root2,leaf2)
        return leaf1==leaf2

