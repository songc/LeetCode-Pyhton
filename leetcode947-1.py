import collections
class Solution:
    def removeStones(self, stones: list) -> int:
        res = 0
        n = len(stones)
        xDict=collections.defaultdict(list)
        yDict = collections.defaultdict(list)
        for v1, v2 in stones:
            xDict[v1].append([v1,v2])
            yDict[v2].append([v1,v2])
        visited = set()
        def dfs(x,y):
            if (x,y) in visited:
                return
            visited.add((x,y))
            for v1, v2 in xDict[x]:
                dfs(v1,v2)
            for v1, v2 in yDict[y]:
                dfs(v1,v2)
        for v1,v2 in stones:
            if (v1,v2) in visited:
                continue
            res+=1
            dfs(v1,v2)
            if len(visited)==n:
                break
        return n-res