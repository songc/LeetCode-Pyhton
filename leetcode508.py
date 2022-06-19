# 508. 出现次数最多的子树元素和
# 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

# 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/most-frequent-subtree-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        vdict = collections.defaultdict(int)
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = left+right+node.val
            vdict[s]+=1
            return s
        dfs(root)
        target=max(vdict[v] for v in vdict)
        ans = [i for i in vdict if vdict[i]==target]
        return ans