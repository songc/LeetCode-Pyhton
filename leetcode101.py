# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

def createTreeFromList(nums):
    treeNode=dict()
    for i in range(len(nums)-1,-1,-1):
        if nums[i]:
            left = right =None
            if 2*i+1 in treeNode:
                left = treeNode[2*i+1]
            if 2*(i+1) in treeNode:
                right = treeNode[2*(i+1)]
            tmp = TreeNode(nums[i],left,right)
            treeNode[i]=tmp
    return treeNode[0]
        

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # treeNum = []
        # def midOrder(tree):
        #     if tree is None:
        #         treeNum.append(None)
        #         return
        #     if tree.left or tree.right:
        #         midOrder(tree.left)
        #         treeNum.append(tree.val)
        #         midOrder(tree.right)
        #     else:
        #         treeNum.append(tree.val)
        # midOrder(root)
        # left,right = 0, len(treeNum)-1
        # if len(treeNum)%2==0:
        #     return False
        # while left<right:
        #     if treeNum[left] != treeNum[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True
        
        def isSyme(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 is None or tree2 is None:
                return False
            return tree1.val==tree2.val and isSyme(tree1.left,tree2.right) and isSyme(tree1.right,tree2.left)
        if root is None:
            return True
        return isSyme(root.left,root.right)
            

sol = Solution()
nums = [1,2,2,3,4,4,3]
root = createTreeFromList(nums)
print(sol.isSymmetric(root))