# 399. 除法求值
# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/evaluate-division
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equaDict = collections.defaultdict(dict)
        ans = []
        def update(x,y,val):
            if (x,y) in equaDict[x] or (y,x) in equaDict[y]:
                return
            equaDict[x][(x,y)]=val
            equaDict[y][(y,x)]=1/val
            xKeyList = [k for k in equaDict[x].keys()]
            for k in xKeyList:
                if k[1] == y:
                    continue
                update(k[1],y,val/equaDict[x][k])
            yKeyList = [k for k in equaDict[y].keys()]
            for z in yKeyList:
                if z[1]==x:
                    continue
                update(z[1],x,1/val/equaDict[y][z])

        for eque, val in zip(equations,values):
            x,y = eque[0],eque[1]
            if x not in equaDict:
                equaDict[x][(x,x)]=1.0
            if y not in equaDict:
                equaDict[y][(y,y)]=1.0
            update(x,y,val)
        for x,y in queries:
            if x not in equaDict or y not in equaDict:
                ans.append(-1.0)
                continue
            if x in equaDict and (x,y) not in equaDict[x]:
                ans.append(-1.0)
                continue
            ans.append(equaDict[x][(x,y)])
        return ans

sol = Solution()
# equations= [["a","e"],["b","e"]]
# values = [4.0,3.0]
# queries = [["a","b"],["e","e"],["x","x"]]
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(sol.calcEquation(equations,values,queries))


            