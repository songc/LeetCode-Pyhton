# 105. 从前序与中序遍历序列构造二叉树

# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        ind = inorder.index(preorder[0])
        leftIn =  []
        rightIn = []
        leftPre = []
        rightPre = []
        if ind == 0:
            rightIn =  inorder[ind+1:]
            rightPre = preorder[1:]
        elif ind>0 and ind<len(inorder)-1:
            leftIn = inorder[:ind]
            rightIn = inorder[ind+1:]
            leftSet = set(leftIn)
            for x in preorder[1:]:
                if x in leftSet:
                    leftPre.append(x)
                else:
                    rightPre.append(x)
        else:
            leftIn = inorder[:ind]
            leftPre = preorder[1:]
        left = self.buildTree(leftPre,leftIn)
        right = self.buildTree(rightPre,rightIn)
        return TreeNode(preorder[0],left,right)

sol = Solution()
preorder = [3,2,1,4]
inorder = [1,2,3,4]
sol.buildTree(preorder,inorder)