# 1342. 将数字变成 0 的操作次数
# 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

class Solution:
    def numberOfSteps(self, num: int) -> int:
        s1 = bin(num)
        return len(s1)+s1.count('1')-3

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(s1:=bin(num))+s1.count('1')-3