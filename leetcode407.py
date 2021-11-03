# 407. 接雨水 II
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m,n=len(heightMap),len(heightMap[0])
        if n<=2 or m<=2:
            return 0
        visited =[[0 for _ in range(n)] for _ in range(m)]
        deque = []
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    heapq.heappush(deque,(heightMap[i][j],i,j))
                    visited[i][j]=1
        diff = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0 
        while deque:
            height,x,y = heapq.heappop(deque)
            for i,j in diff:
                nx,ny = x+i,y+j
                if nx>=0 and nx<m and ny>=0 and ny<n and visited[nx][ny]==0:
                    if height>heightMap[nx][ny]:
                        res+=height-heightMap[nx][ny]
                    heapq.heappush(deque,(max(heightMap[nx][ny],height),nx,ny))
                    visited[nx][ny]=1
        return res

sol = Solution()
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(sol.trapRainWater(heightMap))
