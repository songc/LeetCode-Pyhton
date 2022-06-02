# 450. 删除二叉搜索树中的节点
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

# 一般来说，删除节点可分为两个步骤：

# 首先找到需要删除的节点；
# 如果找到了，删除它。


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/delete-node-in-a-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            tmp = root.right
            while tmp.left:
                tmp=tmp.left
            tmp.left=root.left
            root=root.right
        return root