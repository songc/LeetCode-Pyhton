# 959. 由斜杠划分区域
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。

# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。

# 返回区域的数目。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regions-cut-by-slashes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def regionsBySlashes(self, grid: list) -> int:
        n = len(grid)
        parent = [i for i in range(4*n*n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            parent[rootY]=rootX
        
        for i in range(n):
            for j in range(n):
                ind = 4*(i*n+j)
                if grid[i][j]=="/":
                    union(ind,ind+3)
                    union(ind+1,ind+2)
                elif grid[i][j]=="\\":
                    union(ind,ind+1)
                    union(ind+2,ind+3)
                elif grid[i][j]==" ":
                    union(ind,ind+1)
                    union(ind+2,ind+3)
                    union(ind,ind+2)
                if i<n-1:
                    ind2=4*((i+1)*n+j)
                    union(ind+2,ind2)
                if j<n-1:
                    ind2 = 4*(i*n+(j+1))
                    union(ind+1,ind2+3)
        vset = set()
        for i in range(4*n*n):
            vset.add(find(i))
        return len(vset) 

sol = Solution()
grid=[
  " /",
  "/ "
]
print(sol.regionsBySlashes(grid))
