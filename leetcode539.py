# 539. 最小时间差
# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

from re import S
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        allM = 24*60
        res = 24*60
        n = len(timePoints)
        for i in range(1,n):
            if timePoints[i]==timePoints[i-1]:
                return 0
            h1,m1=timePoints[i].split(":")
            h2,m2=timePoints[i-1].split(":")
            diffh=int(h1)-int(h2)
            diffm = int(m1)-int(m2)
            tmp = diffh*60+diffm
            res = min(res,tmp)
        h1,m1=timePoints[-1].split(":")
        h2,m2=timePoints[0].split(":")
        diffh=int(h1)-int(h2)
        diffm = int(m1)-int(m2)
        tmp = diffh*60+diffm
        res = min(res,tmp,allM-tmp)
        return res

sol = Solution()
timePoints = ["00:00","04:00","22:00"]
print(sol.findMinDifference(timePoints))
        

