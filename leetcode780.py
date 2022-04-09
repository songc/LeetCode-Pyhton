# 780. 到达终点
# 给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。

# 从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reaching-points
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 超时
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>0 and ty>0:
            if tx==sx and ty==sy:
                return True
            if tx>ty:
                tx = tx-ty
            else:
                ty = ty-tx
        return False


class Solution2:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>=sx and ty>=sy:
            if tx==sx and ty==sy:
                return True
            if tx>ty:
                nx=sx+(tx-sx)%ty
                if nx==tx:
                    return False
                tx=nx
            else:
                ny = sy+(ty-sy)%tx
                if ny==ty:
                    return False
                ty=ny
        return False
             

sol = Solution2()
sx = 10
sy = 9
tx = 19
ty = 9
print(sol.reachingPoints(sx,sy,tx,ty))