class Solution:
    def intToRoman(self, num: int) -> str:
        baseList = [1000,100,10,1]
        baseDict= {
            1000:"M",
            500:"D",
            100:"C",
            50:"L",
            10:"X",
            5:"V",
            1:"I"
        }
        res=[]
        for ind,base in enumerate(baseList):
            t = num//base
            num = num%base
            if t>0 and base==1000:
                res.append(baseDict[base]*t)
                continue
            if t<4:
                res.append(baseDict[base]*t)
            elif t==4:
                res.append(baseDict[base]+baseDict[base*5])
            elif t==5:
                res.append(baseDict[base*5])
            elif t<9:
                res.append(baseDict[base*5]+baseDict[base]*(t-5))
            elif t==9:
                res.append(baseDict[base]+baseDict[baseList[ind-1]])
        return "".join(res)
            

