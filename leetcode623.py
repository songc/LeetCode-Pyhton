# 623. 在二叉树中增加一行
# 给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。

# 注意，根节点 root 位于深度 1 。

# 加法规则如下:

# 给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。
# cur 原来的左子树应该是新的左子树根的左子树。
# cur 原来的右子树应该是新的右子树根的右子树。
# 如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/add-one-row-to-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root)
        curDep = 1
        curNode = [root]
        while curDep<depth-1:
            nextNode = []
            for node in curNode:
                if node.left:
                    nextNode.append(node.left)
                if node.right:
                    nextNode.append(node.right)
            curNode=nextNode
            curDep+=1
        for node in curNode:
            node.left=TreeNode(val,node.left)
            node.right=TreeNode(val,None,node.right)
        return root