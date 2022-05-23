# 675. 为高尔夫比赛砍树
# 你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：

# 0 表示障碍，无法触碰
# 1 表示地面，可以行走
# 比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
# 每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。

# 你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。

# 你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。

# 可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/cut-off-trees-for-golf-event
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        visted = set()
        def dfs(startX,startY,target):
            if forest[startX][startY]==target:
                return 0
            deque = collections.deque()
            deque.append((startX,startY,0))
            diff = [(1,0),(0,1),(-1,0),(0,-1)]
            while deque:
                x,y,step = deque.popleft()
                for dx,dy in diff:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<len(forest) and 0<=ny<len(forest[0]) and (nx,ny) not in visted:
                        visted.add((nx,ny))
                        if forest[nx][ny]==0:
                            continue
                        elif forest[nx][ny]==target:
                            return step+1
                        else:
                            deque.append((nx,ny,step+1))
            return -1
        m, n = len(forest), len(forest[0])
        vDict = dict()
        for i in range(m):
            for j in range(n):
                if forest[i][j]>1:
                    vDict[forest[i][j]]=(i,j)
        vlist = sorted(vDict.keys())
        pre = (0,0)
        ans = 0
        for v in vlist:
            visted = set()
            step = dfs(pre[0],pre[1],v)
            if step>=0:
                ans+=step
                pre = vDict[v]
            else:
                return -1
        return ans


sol = Solution()
forest = [[2,3,4],[0,0,5],[8,7,6]]
print(sol.cutOffTree(forest))
                        
                            

        