# 447. 回旋镖的数量
# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

# 返回平面上所有回旋镖的数量。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-boomerangs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        dist = [collections.defaultdict(list) for _ in range(n)]
        for i in range(n-1):
            x,y = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                tmp = (x2-x)**2+(y2-y)**2
                dist[i][tmp].append(j)
                dist[j][tmp].append(i)
        for i in range(n):
            for key in dist[i]:
                for j in dist[i][key]:
                    res+=len(dist[j][key])-1
        return res

class Solution2:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for x,y in points:
            dist = collections.defaultdict(int)
            for x1,y1 in points:
                tmp = (x1-x)**2+(y1-y)**2
                dist[tmp]+=1
            for d in dist.values():
                res+=d*(d-1)
        return res


sol = Solution2()
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
print(sol.numberOfBoomerangs(points))
