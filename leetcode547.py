class Solution:
    def findCircleNum(self, isConnected: list) -> int:
        citys = set([i for i in range(len(isConnected))])
        res = 0
        while(citys):
           i = citys.pop()
           iset=set()
           self.findConnec(isConnected,i,iset)
           citys.difference_update(iset)
           res+=1
        return res
    def findConnec(self, isConnected:list, i, iset:set):
        if i not in iset:
            iset.add(i)
        for ind, val in enumerate(isConnected[i]):
            if val==1 and ind not in iset:
                self.findConnec(isConnected, ind, iset)
        return iset
sol= Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(sol.findCircleNum(isConnected))
        