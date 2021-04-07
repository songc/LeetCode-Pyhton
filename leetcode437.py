# 437. 路径总和 III
# 给定一个二叉树，它的每个结点都存放着一个整数值。

# 找出路径和等于给定数值的路径总数。

# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections

from TreeNodeUtil import createTreeFromList

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(tree):
            if tree is None:
                return [],[]
            left = dfs(tree.left)
            right = dfs(tree.right)
            has=[]
            for i in left[0]:
                has.append(i+tree.val)
            for i in right[0]:
                has.append(i+tree.val)
            has.append(tree.val)
            return has,left[0]+left[1]+right[0]+right[1]
        sumAll = dfs(root)
        counter = collections.Counter(sumAll[0]+sumAll[1])
        if sum in counter:
            return counter[sum]
        return 0

class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        preSum = collections.defaultdict(int)
        preSum[0]+=1
        def dfs(currSum, node, target):
            if node is None:
                return 0
            currSum +=node.val
            res = 0
            res += preSum[currSum-target]
            preSum[currSum]+=1
            res+=dfs(currSum,node.left,target)
            res+=dfs(currSum,node.right,target)

            preSum[currSum]-=1
            return res
        return dfs(0,root,sum)



nums = [10,5,-3,3,2,None,11,3,-2,None,1]

sol = Solution2()
print(sol.pathSum(createTreeFromList(nums),8))

