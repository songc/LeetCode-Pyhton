# 1161. 最大层内元素和
# 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

# 请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum=root.val
        ans = 1
        level=1
        queue = [root]
        while queue:
            tmp = 0
            nextQueue = []
            for n in queue:
                tmp+=n.val
                if n.left:
                    nextQueue.append(n.left)
                if n.right:
                    nextQueue.append(n.right)
            if tmp>maxSum:
                maxSum=tmp
                ans=level
            level+=1
            queue=nextQueue
        return ans