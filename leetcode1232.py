# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        n=len(coordinates)
        rate=None
        for i in range(1,n):
            dx=coordinates[i][0]-coordinates[i-1][0]
            dy=coordinates[i][1]-coordinates[i-1][1]
            if dx==0:
                newRate=float('inf')
            else:
                newRate=dy/dx
            if rate==None:
                rate=newRate
                continue
            if newRate!=rate:
                return False
        return True