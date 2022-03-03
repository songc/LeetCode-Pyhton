# 258. 各位相加
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。


class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        tmp = 0
        while num:
            tmp=tmp+num%10
            num//=10
        return self.addDigits(tmp)

class Solution2:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        if num%9==0:
            return 9
        return num%9