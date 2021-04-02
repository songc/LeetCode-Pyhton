# 947. 移除最多的同行或同列石头
# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
class Solution:
    def removeStones(self, stones: list) -> int:
        res = 0
        n = len(stones)
        vDict=collections.defaultdict(list)
        v2Dict = collections.defaultdict(list)
        for v1, v2 in stones:
            vDict[v1].append(v2)
            v2Dict[v2].append(v1)
        visited = set()
        def findEdgeV(tv1):
            for tv2 in vDict[tv1]:
                if (tv1,tv2) not in visited:
                    visited.add((tv1,tv2))
                    findEdgeV2(tv2)
        def findEdgeV2(fv2):
            for fv1 in v2Dict[fv2]:
                if (fv1,fv2) not in visited:
                    visited.add((fv1,fv2))
                    findEdgeV(fv1)
        for v1, v2 in stones:
            if (v1,v2) not in visited:
                res+=1
                findEdgeV(v1)
                if len(visited)==n:
                    return n-res
        return n-res 

sol = Solution()
stones=[[0,1],[1,0],[1,1]]
print(sol.removeStones(stones))