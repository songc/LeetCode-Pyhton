import collections
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        def find(i):
            if parent[i]!=i:
                #路径压缩
                parent[i]=find(parent[i])
            return parent[i]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            parent[rootY]=rootX
        for x,y in pairs:
            union(x,y)
        unionDict = collections.defaultdict(list)
        for i in range(n):
            root = find(i)
            unionDict[root].append(i)
        res = list(s)
        for value in unionDict.values():
            chars = sorted(res[i] for i in value)
            for val, char in zip(value,chars):
                res[val]=char
        return "".join(res)

sol=Solution()
s = "cba"
pairs = [[0,1],[1,2]]
print(sol.smallestStringWithSwaps(s,pairs))        