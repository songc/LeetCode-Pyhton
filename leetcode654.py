# 654. 最大二叉树
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
# 返回 nums 构建的 最大二叉树 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        val = max(nums)
        root = TreeNode(val=val)
        numsLeft = []
        numsRight = []
        flag = True
        for v in nums:
            if v ==val:
                flag=False
                continue
            if flag:
                numsLeft.append(v)
            else:
                numsRight.append(v)
        root.left=self.constructMaximumBinaryTree(numsLeft)
        root.right=self.constructMaximumBinaryTree(numsRight)
        return root
        