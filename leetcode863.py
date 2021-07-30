# 863. 二叉树中所有距离为 K 的结点
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from TreeNode import createTreeFromList

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        targetParent= []
        
        def findKNode(node,k):
            if not node:
                return
            if k<0:
                return 
            if k==0:
                res.append(node.val)
                return
            findKNode(node.left,k-1)
            findKNode(node.right,k-1)
        def findNode(node,target):
            if not node:
                return
            if node == target:
                targetParent.append(node)
                return True
            l = findNode(node.left,target)
            r = findNode(node.right,target)
            if l or r:
                targetParent.append(node)
                return True
        findNode(root,target)
        findKNode(target,k)
        n = len(targetParent)
        for i in range(1,k+1):
            if i<n:
                node = targetParent[i]
                if k-i==0:
                    res.append(node.val)
                if node.left == targetParent[i-1]:
                    findKNode(node.right,k-i-1)
                else:
                    findKNode(node.left,k-i-1)
        return res

sol = Solution()
root = [0,None,1,None,2,None,3,4]
K = 2
treeRoot = createTreeFromList(root)
target = treeRoot.right.right
print(sol.distanceK(treeRoot,target,K))
