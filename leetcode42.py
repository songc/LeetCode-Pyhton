# 42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
class Solution:
    def trap(self, height: list) -> int:
        queue = list()
        ans = 0
        for i in range(len(height)):
            while queue and height[i]> height[queue[-1]]:
                ind = queue[-1]
                queue.pop()
                if not queue:
                    break
                dist = i-queue[-1]-1
                hi = min([height[i],height[queue[-1]]])-height[ind]
                ans += dist*hi
            queue.append(i)
        return ans

sol = Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
            