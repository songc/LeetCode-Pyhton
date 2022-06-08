# 1037. 有效的回旋镖
# 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，如果这些点构成一个 回旋镖 则返回 true 。

# 回旋镖 定义为一组三个点，这些点 各不相同 且 不在一条直线上 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-boomerang
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        vset =set( (i,j) for i,j in points)
        if len(vset)<3:
            return False
        dx1,dy1 = points[1][0]-points[0][0],points[1][1]-points[0][1]
        dx2,dy2 = points[2][0]-points[1][0],points[2][1]-points[1][1]
        if dy1==dy2==0:
            return False
        if dy1==0 or dy2==0:
            return True
        if dx1/dy1==dx2/dy2:
            return False
        return True




class Solution2:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dx1,dy1 = points[1][0]-points[0][0],points[1][1]-points[0][1]
        dx2,dy2 = points[2][0]-points[1][0],points[2][1]-points[1][1]
        return dx1*dy2 != dx2*dy1

sol = Solution()
points = [[1,1],[2,2],[3,3]]
print(sol.isBoomerang(points))
