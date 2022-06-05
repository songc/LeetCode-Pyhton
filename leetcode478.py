# 478. 在圆内随机生成点
# 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。

# 实现 Solution 类:

# Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置 (x_center, y_center) 初始化对象
# randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。
#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/generate-random-point-in-a-circle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 0 < radius <= 108
# -107 <= x_center, y_center <= 107
# randPoint 最多被调用 3 * 104 次

from random import Random, randint, random, randrange


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y= y_center


    def randPoint(self) -> List[float]:
        r1 = random()
        r2 = random()
        if r1*r1+r2*r2>1:
            return self.randPoint()
        ne = [1,-1]
        ne1 = randint(0,1)
        ne2 = randint(0,1)
        return [self.x+ne[ne1]*r1*self.radius,self.y+ne[ne2]*r2*self.radius]
        
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()