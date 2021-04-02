class Solution:
    def prefixesDivBy5(self, A: list) -> list:
        res=[]
        tSum=0
        for a in A:
            tSum=((tSum<<1)+a)%5
            res.append(tSum==0)
        return res
