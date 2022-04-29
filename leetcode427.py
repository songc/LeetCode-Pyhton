# 427. 建立四叉树
# 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。

# 你需要返回能表示矩阵的 四叉树 的根结点。

# 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。

# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。

# 44


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-quad-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.dfs(grid,0,n,0,n)


    def dfs(self, grid, startX, endX, startY, endY):
        res = Node(True,True,None,None,None,None)
        pre = grid[startX][startY]
        if pre:
            res.val = True
        else:
            res.val = False
        res.isLeaf = self.isLeaf(grid,startX, endX, startY, endY)   
        if res.isLeaf:
            return res
        midX = (startX+endX)//2
        midY = (startY+endY)//2
        res.topLeft=self.dfs(grid, startX, midX, startY, midY)
        res.topRight=self.dfs(grid, startX, midX, midY, endY)
        res.bottomLeft=self.dfs(grid, midX, endX, startY,midY)
        res.bottomRight = self.dfs(grid, midX,endX, midY, endY)
        return res
    
    def isLeaf(self, grid, startX, endX, startY, endY):
        pre = grid[startX][startY]
        for i in range(startX,endX):
            for j in range(startY,endY):
                if grid[i][j]!=pre:
                    return False
        return True

                
sol = Solution()
grid = grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
print(sol.construct(grid))