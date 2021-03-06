# 114. 二叉树展开为链表
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def preOrder(treeNode):
            nodes.append(treeNode)
            if treeNode.left:
                preOrder(treeNode.left)
            if treeNode.right:
                preOrder(treeNode.right)
        if root:
            preOrder(root)
        nodes.append(None)
        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        