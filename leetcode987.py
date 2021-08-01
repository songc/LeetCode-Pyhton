# 987. 二叉树的垂序遍历
# 给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。

# 对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。

# 二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。

# 返回二叉树的 垂序遍历 序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
import collections
from TreeNodeUtil import createTreeFromList
import bisect
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        vDict = collections.defaultdict(dict)
        def preOrder(node:TreeNode, row:int, col:int):
            if not node:
                return
            if row in vDict[col]:
                bisect.insort_right(vDict[col][row],node.val)
            else:
                vDict[col][row]=[node.val]
            preOrder(node.left,row+1,col-1)
            preOrder(node.right,row+1,col+1)
        preOrder(root,0,0)
        res = []
        for col in sorted(vDict.keys()):
            tmp = []
            for row in sorted(vDict[col]):
                tmp.extend(vDict[col][row])
            res.append(tmp)
        return res

sol = Solution()
nodeList = [0,8,1,None,None,3,2,None,4,5,None,None,7,6]
root = createTreeFromList(nodeList)
print(sol.verticalTraversal(root))