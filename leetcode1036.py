# 1036. 逃离大迷宫
# 在一个 106 x 106 的网格中，每个网格上方格的坐标为 (x, y) 。

# 现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。

# 每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。

# 只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/escape-a-large-maze
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        n = len(blocked)
        MaxLen = 10**6
        if n<2:
            return True
        blockedSet = set(tuple(x) for x in blocked)
        countDown = n*(n-1)//2
        def check(start, end):
            visited=set()
            visited.add(tuple(start))
            deque = collections.deque()
            deque.append(tuple(start))
            while deque and len(visited)<=countDown:
                x,y = deque.popleft()
                for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    tmp = (nx,ny)
                    if 0<=nx<MaxLen and 0<=ny<MaxLen and tmp not in blockedSet and tmp not in visited:
                        if nx==end[0] and ny==end[1]:
                            return True
                        deque.append(tmp)
                        visited.add(tmp)
            return len(visited)>countDown
        return check(source,target) and check(target,source)

sol = Solution()
blocked = [[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]]
source = [655988,180910]
target = [267728,840949]
print(sol.isEscapePossible(blocked,source,target))
                



        