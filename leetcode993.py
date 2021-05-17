# 993. 二叉树的堂兄弟节点
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root,)]
        while queue:
            newQue = []
            newSet = set()
            for nodes in queue:
                tmpSet = set()
                for node in nodes:
                    if node:
                        newSet.add(node.val)
                        tmpSet.add(node.val)
                        newQue.append((node.left,node.right))
                if x in tmpSet and y in tmpSet:
                    return False
            bx = x in newSet
            by = y in newSet
            if bx and by:
                return True
            if bx or by:
                return False
            
            queue=newQue
        return False
