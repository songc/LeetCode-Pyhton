# 497. 非重叠矩形中的随机点
# 给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，(xi, yi) 是第 i 个矩形的右上角角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。

# 在一个给定的矩形覆盖的空间内任何整数点都有可能被返回。

# 请注意 ，整数点是具有整数坐标的点。

# 实现 Solution 类:

# Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
# int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from bisect import bisect_left
from random import randint, randrange
from typing import List

### 注意要用坐标点数来计算前缀和。不能直接用面积。
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects=rects
        self.preSum=[0]
        for a,b,x,y in rects:
            self.preSum.append(self.preSum[-1]+(x-a+1)*(y-b+1))


    def pick(self) -> List[int]:
        num = randint(1,self.preSum[-1])
        ind = bisect_left(self.preSum,num)
        a,b,x,y= self.rects[ind-1]
        dx = randint(0,x-a)
        dy = randint(0,y-b)
        return [a+dx,b+dy]




# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()