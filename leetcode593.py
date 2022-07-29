# 593. 有效的正方形
# 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。

# 点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。

# 一个 有效的正方形 有四条等边和四个等角(90度角)。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-square
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        t = [p1,p2,p3,p4]
        for i in range(4):
            tmp = []
            for j in range(4):
                x1,y1 = t[i]
                x2,y2 = t[j]
                tmp.append((y1-y2)**2+(x1-x2)**2)
            tmp.sort()
            if tmp[1]==0:
                return False
            if tmp[1]==tmp[2] and tmp[1]+tmp[2]==tmp[3]:
                continue
            return False
        return True

sol = Solution()
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,12]
print(sol.validSquare(p1,p2,p3,p4))