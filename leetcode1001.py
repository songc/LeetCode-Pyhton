# 1001. 网格照明
# 在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。

# 给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。

# 当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。

# 另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj] 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。

# 返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/grid-illumination
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rowDict = collections.defaultdict(int)
        colDict = collections.defaultdict(int)
        sumDict = collections.defaultdict(int)
        diffDict = collections.defaultdict(int)
        lampSet = set()
        for row,col in lamps:
            if (row,col) not in lampSet:
                rowDict[row]+=1
                colDict[col]+=1
                sumDict[row+col]+=1
                diffDict[col-row]+=1
            lampSet.add((row,col))
        ans = []
        diffList = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

        def offLamp(row,col):
            for x,y in diffList:
                nr = row+x
                nc = col+y
                if (nr,nc) in lampSet:
                    lampSet.remove((nr,nc))
                    rowDict[nr]-=1
                    colDict[nc]-=1
                    sumDict[nr+nc]-=1
                    diffDict[nc-nr]-=1
            
        for row,col in queries:
            if row in rowDict and rowDict[row]>0:
                ans.append(1)
            elif col in colDict and colDict[col]>0:
                ans.append(1)
            elif row+col in sumDict and sumDict[row+col]>0:
                ans.append(1)
            elif col-row in diffDict and diffDict[col-row]>0:
                ans.append(1)
            else:
                ans.append(0)
            offLamp(row,col)
        return ans

sol = Solution()
n = 5
lamps = [[0,0],[0,4]]
queries = [[0,4],[0,1],[1,4]]
print(sol.gridIllumination(n,lamps,queries))
            