# 335. 路径交叉
# 给你一个整数数组 distance 。

# 从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

# 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/self-crossing
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        for i in range(3,n):
            a,b,c,d=distance[i],distance[i-1],distance[i-2],distance[i-3]
            if c<=a and d>=b:
                return True
            if i>=4 and b==d and a+distance[i-4]>=c:
                return True
            if i>=5:
                e=distance[i-4]
                f=distance[i-5]
                if b<=d and c>e and a+e>=c and b+f>=d:
                    return True
        return False

sol = Solution()
distance = [2,1,1,2]
print(sol.isSelfCrossing(distance))