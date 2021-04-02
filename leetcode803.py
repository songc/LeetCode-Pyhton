# 803. 打砖块
# 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：

# 一块砖直接连接到网格的顶部，或者
# 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
# 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bricks-falling-when-hit
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def hitBricks(self, grid: list, hits: list) -> list:
        m,n = len(grid),len(grid[0])
        res = []
        def dfs(x,y, visited:set):
            if (x,y) in visited:
                return
            visited.add((x,y))
            if x==0:
                visited.add(True)
                return
            if x-1>=0 and grid[x-1][y]==1:
                dfs(x-1,y,visited)
            if x+1<m and grid[x+1][y]==1:
                dfs(x+1,y,visited)
            if y+1<n and grid[x][y+1]==1:
                dfs(x,y+1,visited)
            if y-1>=0 and grid[x][y-1]==1:
                dfs(x,y-1,visited)
        def init0(visited:set):
            for x,y in visited:
                grid[x][y]=0
        for x,y in hits:
            if grid[x][y]==0:
                res.append(0)
            else:
                grid[x][y]=0
                tmp = 0
                if x-1>=0 and grid[x-1][y]==1:
                    visited=set()
                    dfs(x-1,y,visited)
                    if True  not in visited:
                        tmp+=len(visited)
                        init0(visited)
                if x+1<m and grid[x+1][y]==1:
                    visited=set()
                    dfs(x+1,y,visited)
                    if True  not in visited:
                        tmp+=len(visited)
                        init0(visited)
                if y-1>=0 and grid[x][y-1]==1:
                    visited=set()
                    dfs(x,y-1,visited)
                    if True  not in visited:
                        tmp+=len(visited)
                        init0(visited)
                if y+1<n and grid[x][y+1]==1:
                    visited=set()
                    dfs(x,y+1,visited)
                    if True  not in visited:
                        tmp+=len(visited)
                        init0(visited)
                res.append(tmp)
        return res

sol=Solution()
grid=[[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
print(sol.hitBricks(grid,hits))
        
            
        