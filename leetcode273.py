# 273. 整数转换英文表示
# 将非负整数 num 转换为其对应的英文表示。

class Solution:
    def numberToWords(self, num: int) -> str:
        numList = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        num2List = ['',"Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        num3List = ["Hundred"]
        specialNum= ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen", "Sixteen", "Seventeen","Eighteen","Nineteen"]
        unit = ["Thousand","Million","Billion"]
        if num<10:
            return numList[num]
        if num<20:
            return specialNum[num-10]
        res = []
        strNum = str(num)
        n = len(strNum)
        i=0
        while i < n:
            ind = int(strNum[i])
            div,mod = divmod(n-i,3)
            if ind==0:
                if mod==1 and div>0 and res[-1] not in set(unit):
                    res.append(unit[div-1])
                i+=1
                continue
            if mod==0:
                res.append(numList[ind])
                res.append(num3List[0])
            elif mod==2:
                if ind==1:
                    i+=1
                    ind = int(strNum[i])
                    res.append(specialNum[ind])
                    if div>0:
                        res.append(unit[div-1])
                else:
                    res.append(num2List[ind])
            elif mod==1:
                res.append(numList[ind])
                if div>0:
                    res.append(unit[div-1])
            i+=1
        return " ".join(res)

sol = Solution()
num = 1000000
print(sol.numberToWords(num))



