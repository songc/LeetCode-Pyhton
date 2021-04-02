class Solution:
    def romanToInt(self, s: str) -> int:
        dictBase = dict([("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",40),
        ("X",10),("IX",9),("V",5),("IV",4),("I",1)])
        i=0
        res=0
        while(i<len(s)):
            if i<len(s)-1 and  s[i:i+2] in dictBase:
                res+=dictBase[s[i:i+2]]
                i+=2
            else:
                res+=dictBase[s[i]]
                i+=1
        return res
sol=Solution()
s ="MCMXCIV"
print(sol.romanToInt(s))