# 1765. 地图中的最高点
# 给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。

# 如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
# 如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。
# 你需要按照如下规则给每个单元格安排高度：

# 每个格子的高度都必须是非负的。
# 如果一个格子是是 水域 ，那么它的高度必须为 0 。
# 任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
# 找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。

# 请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/map-of-highest-peak
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n = len(isWater),len(isWater[0])
        height=[[float('inf')]*n for _ in range(m)]
        deque = collections.deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    deque.append((i,j))
                    height[i][j]=0
        diff = [(1,0),(-1,0),(0,1),(0,-1)]
        while deque:
            i,j=deque.popleft()
            for x,y in diff:
                nx = i+x
                ny = j+y
                if 0<=nx<m and 0<=ny<n and height[nx][ny]==float('inf'):
                    deque.append((nx,ny))
                    height[nx][ny]=height[i][j]+1
        return height

sol = Solution()
isWater = [[0,1],[0,0]]
print(sol.highestPeak(isWater))
        