# 84. 柱状图中最大的矩形
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
import bisect
class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        ans = 0
        deque = []
        deque.append(0)
        tmpList = [0]+heights+[0]
        for i in range(1,len(tmpList)):
            while tmpList[i]<tmpList[deque[-1]]:
                hi = tmpList[deque.pop()]
                width = i-deque[-1]-1
                ans=max(ans,hi*width)
            deque.append(i)
        return ans
            
 
sol =Solution() 
height=[1,2,3,4,5,6,7]
print(sol.largestRectangleArea(height))
