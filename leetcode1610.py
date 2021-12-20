# 1610. 可见点的最大数目

# 给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，其中 location = [posx, posy] 且 points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。

# 最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，posx 和 posy 不能改变。你的视野范围的角度用 angle 表示， 这决定了你观测任意方向时可以多宽。设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。

# 对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。

# 同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。

# 返回你能看到的点的最大数目。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-visible-points
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。
from typing import List
from math import atan2, pi
import bisect

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        sameCnt=0
        angleList= []
        for point in points:
            if point==location:
                sameCnt+=1
            else:
                angleList.append(atan2(point[1]-location[1],point[0]-location[0]))
        angleList.sort()
        n = len(angleList)
        for i in range(n):
            angleList.append(angleList[i]+2*pi)
        degree = angle/180*pi
        maxCount = max((bisect.bisect_right(angleList, angleList[i]+degree)-i for i in range(n)),default=0)
        return maxCount+sameCnt

sol = Solution()
points = [[2,1],[2,2],[3,3]]
angle = 90
location = [1,1]
print(sol.visiblePoints(points,angle,location))
