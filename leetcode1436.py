# 1436. 旅行终点站

# 给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

# 题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/destination-city
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pDict = collections.defaultdict(int)
        for f,t in paths:
            pDict[f]+=1
            if t not in pDict:
                pDict[t]=0
        for k in pDict:
            if pDict[k]==0:
                return k

sol =Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sol.destCity(paths))
        