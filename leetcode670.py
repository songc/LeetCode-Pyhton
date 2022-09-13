# 670. 最大交换
# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

class Solution:
    def maximumSwap(self, num: int) -> int:
        clist = [c for c in str(num)]
        n = len(clist)
        for i in range(n-1):
            tmpM = clist[i]
            ind = i
            for j in range(i+1,n):
                if ind ==i and clist[j]>tmpM:
                    tmpM=clist[j]
                    ind=j
                elif ind>i and clist[j]>=tmpM:
                    tmpM=clist[j]
                    ind=j
            if ind>i:
                clist[i],clist[ind]=clist[ind],clist[i]
                break
        return int("".join(clist))
