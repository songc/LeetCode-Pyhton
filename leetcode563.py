# 563. 二叉树的坡度
# 给定一个二叉树，计算 整个树 的坡度 。

# 一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。

# 整个树 的坡度就是其所有节点的坡度之和。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-tilt
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        nodes = []

        def lastorder(node):
            if not node:
                return 0
            sumleft = lastorder(node.left)
            sumright = lastorder(node.right)
            nodes.append(abs(sumleft-sumright))
            return node.val+sumright+sumleft
        lastorder(root)
        return sum(nodes)

