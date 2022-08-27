# 662. 二叉树最大宽度
# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

# 树的 最大宽度 是所有层中最大的 宽度 。

# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。

# 题目数据保证答案将会在  32 位 带符号整数范围内。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-width-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        queue = [(0,root)]
        while queue:
            nextQueue = []
            for i,node in queue:
                if node.left:
                    nextQueue.append((i*2+1,node.left))
                if node.right:
                    nextQueue.append((i*2+2,node.right))
            if len(nextQueue)>=2:
                ans = max(ans,nextQueue[-1][0]-nextQueue[0][0]+1)
            queue=nextQueue
        return ans
