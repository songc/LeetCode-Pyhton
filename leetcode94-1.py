class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def inOrder(tree):
            if tree is None:
                return
            inOrder(tree.left)
            ans.append(tree.val)
            inOrder(tree.right)
        inOrder(root)
        return ans