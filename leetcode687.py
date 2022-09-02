# 687. 最长同值路径
# 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。

# 两个节点之间的路径长度 由它们之间的边数表示。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-univalue-path
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def getMaxPath(node, target, cnt):
            nonlocal ans
            if not node:
                return cnt
            if node.val==target:
                left = getMaxPath(node.left,target,cnt+1)
                right = getMaxPath(node.right,target,cnt+1)
                ans = max(left+right-2*cnt-2,ans)
                return max(left,right)
            else:
                left = getMaxPath(node.left,node.val,0)
                right = getMaxPath(node.right,node.val,0)
                ans = max(left+right,ans)
                return cnt
        getMaxPath(root,-1,0)
        return ans
