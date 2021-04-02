# 721. 账户合并
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。

# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。

# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/accounts-merge
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
class Solution:
    def accountsMerge(self, accounts: list) -> list:
        accountDict = collections.defaultdict(list)
        for ind, account in  enumerate(accounts):
            for s in account[1:]:
                accountDict[s].append(ind)
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
        def merge(ind):
            if ind in visted:
                return
            for s in accounts[ind][1:]:
                for ind2 in accountDict[s]:
                    visted.add(ind)
                    union(ind,ind2)
                    merge(ind2)
        visted=set()
        for i in range(len(accounts)):
            merge(i)
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

        
        