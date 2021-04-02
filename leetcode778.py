# 778. 水位上升的泳池中游泳
# 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

# 现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

# 你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/swim-in-rising-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def swimInWater(self, grid: list) -> int:
        n = len(grid)
        parent=[i for i in range(n*n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(y)]=find(x)
        edges=[]
        for i in range(n):
            for j in range(n):
                if i>0:
                    edges.append([(i-1)*n+j,i*n+j, max([grid[i-1][j],grid[i][j]])])
                if j>0:
                    edges.append([i*n+j-1,i*n+j, max([grid[i][j-1],grid[i][j]])])
        edgeSorted = sorted(edges, key=lambda x:x[-1])
        for edge in edgeSorted:
            union(edge[0],edge[1])
            if find(0)==find(n*n-1):
                return edge[-1]
sol = Solution()
grid=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(sol.swimInWater(grid))