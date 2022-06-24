# 515. 在每个树行中找最大值
# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root:
            return ans
        queue = []
        queue.append(root)
        ans.append(root.val)
        while queue:
            tmp = []
            for n in queue:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            queue = tmp
            if tmp:
                ans.append(max(n.val for n in tmp))
        return ans
                
