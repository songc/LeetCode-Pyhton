# 面试题 17.21. 直方图的水量
# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                ind = stack.pop()
                if not stack:
                    break
                width = i-stack[-1]-1
                hi = min(height[i],height[stack[-1]])-height[ind]
                ans += hi*width
            stack.append(i)
        return ans

sol = Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))