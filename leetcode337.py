# 337. 打家劫舍 III
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
from functools import lru_cache
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 有点慢，但是过了
class Solution:
    
    def rob(self, root: TreeNode) -> int:

        @lru_cache()
        def dfs(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.val
            left = 0
            right = 0
            if root.left:
                left = self.rob(root.left.left)+self.rob(root.left.right)
            
            if root.right:
                right = self.rob(root.right.left)+self.rob(root.right.right)
            return max(left+right+root.val,self.rob(root.left)+self.rob(root.right))
        return dfs(root)
            
class Solution2:
    
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        deque = collections.deque()
        deque.append(root)
        nodeDict = dict()
        nodes = []
        while deque:
            node = deque.popleft()
            nodes.append(node)
            nodeDict[node]=0
            if node:
                deque.append(node.left)
                deque.append(node.right)
        def maxCore(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val
            left = 0
            right = 0
            if node.left:
                left = nodeDict.get(node.left.left)+nodeDict.get(node.left.right)
            
            if node.right:
                right = nodeDict.get(node.right.left)+nodeDict.get(node.right.right)

            return max(left+right+node.val,nodeDict.get(node.left)+nodeDict.get(node.right))
        n = len(nodes)
        for i in range(n-1,-1,-1):
            nodeDict[nodes[i]]=maxCore(nodes[i])
        return nodeDict[root]
                
        