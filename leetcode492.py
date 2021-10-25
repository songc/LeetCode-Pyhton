# 492. 构造矩形
# 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：
# 1. 你设计的矩形页面必须等于给定的目标面积。

# 2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。

# 3. 长度 L 和宽度 W 之间的差距应当尽可能小。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-the-rectangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        begin = int(area**0.5)
        if begin**2==area:
            return [begin,begin]
        for i in range(begin+1,area+1):
            div,mod = divmod(area,i)
            if mod==0:
                return [i,div]

class Solution2:
    def constructRectangle(self, area: int) -> List[int]:
        begin = int(area**0.5)
        for i in range(begin,0,-1):
            div,mod = divmod(area,i)
            if mod==0:
                return [div,i]

sol = Solution2()
print(sol.constructRectangle(9))