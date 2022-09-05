# 652. 寻找重复的子树
# 给定一棵二叉树 root，返回所有重复的子树。
# 对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 如果两棵树具有相同的结构和相同的结点值，则它们是重复的。
#  
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-duplicate-subtrees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        vdict = collections.defaultdict(list)
        
        def ord(node):
            if not node:
                return ''
            left = ord(node.left)
            right = ord(node.right)
            ans = "(%s)%d(%s)"%(left,node.val,right)
            vdict[ans].append(node)
            return ans
        ord(root)
        ans = []
        for v in vdict:
            if len(vdict[v])>=2:
                ans.append(vdict[v][0])
        return ans