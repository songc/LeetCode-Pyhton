# 812. 最大三角形面积
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。


from itertools import combinations
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(x1,y1,x2,y2,x3,y3):
            return 0.5*abs(x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1)
        return max(triangleArea(x1,y1,x2,y2,x3,y3) for (x1,y1),(x2,y2),(x3,y3) in combinations(points,3))