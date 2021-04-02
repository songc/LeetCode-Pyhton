import collections
class Solution:
    def accountsMerge(self, accounts: list) -> list:
        accountDict = collections.defaultdict(list)
        parent=[i for i in range(len(accounts))]
        def find(i):
            if parent[i]!=i:
                parent[i]=find(parent[i])
            return parent[i]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY]=rootX
        for ind, account in  enumerate(accounts):
            for s in account[1:]:
                accountDict[s].append(ind)
                if len(accountDict[s])>=2:
                    union(accountDict[s][-2],accountDict[s][-1])       
        indDict=collections.defaultdict(list)
        for i in range(len(parent)):
            indDict[find(i)].append(i)
        res=[]
        for key,value in indDict.items():
            tmp=[]
            tmp.append(accounts[key][0])
            tmp2 = set()
            for ind in value:
                tmp2.update(accounts[ind][1:])
            tmp.extend(sorted(tmp2))
            res.append(tmp)
        return res
        
sol = Solution()
accounts= [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(sol.accountsMerge(accounts))