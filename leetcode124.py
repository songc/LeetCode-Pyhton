# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        nodes = []
        dp = dict()
        ans = root.val
        def lastOrder(tree):
            if tree is None:
                return
            lastOrder(tree.left)
            lastOrder(tree.right)
            nodes.append(tree)
        lastOrder(root)
        for node in nodes:
            dp[hash(node)]=0
        for i in range(len(nodes)):
            node = nodes[i]
            left = 0
            right = 0
            if node.left:
                left = dp[hash(node.left)]
            if node.right:
                right = dp[hash(node.right)]
            dp[hash(node)]=max(left+node.val,right+node.val,0)
            ans = max(ans, node.val+left+right)
        return ans
        
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

sol = Solution()
nums = [1,2,3]
root = createTreeFromList(nums)
print(sol.maxPathSum(root))