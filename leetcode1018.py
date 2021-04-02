class Solution:
    def prefixesDivBy5(self, A: list) -> list:
        res=[]
        tSum=0
        for a in A:
            tSum=tSum*2+a
            if tSum%5==0:
                res.append(True)
            else:
                res.append(False)
        return res
