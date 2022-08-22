# 655. 输出二叉树
# 给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局 。构造此格式化布局矩阵需要遵循以下规则：

# 树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。
# 矩阵的列数 n 应该等于 2height+1 - 1 。
# 根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。
# 对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2height-r-1] ，右子节点放置在 res[r+1][c+2height-r-1] 。
# 继续这一过程，直到树中的所有节点都妥善放置。
# 任意空单元格都应该包含空字符串 "" 。
# 返回构造得到的矩阵 res 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/print-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.getHeight(root)
        ans = [[""]*(2**height-1) for _ in range(height)]
        q = [(root,(2**height-2)//2)]
        ans[0][q[0][1]]=str(root.val)
        curH = 1
        while q:
            nextQ= []
            for n,c in q:
                if n.left:
                    pos = c-2**(height-curH-1)
                    ans[curH][pos]=str(n.left.val)
                    nextQ.append((n.left,pos))
                if n.right:
                    pos = c+2**(height-curH-1)
                    ans[curH][pos]=str(n.right.val)
                    nextQ.append((n.right,pos))
            curH+=1
            q=nextQ
        return ans

    
    def getHeight(self, root: TreeNode) -> int :
        ans = 0
        q = [root]
        while q:
            nextQ = []
            for n in q:
                if n.left:
                    nextQ.append(n.left)
                if n.right:
                    nextQ.append(n.right)
            ans += 1
            q = nextQ
        return ans