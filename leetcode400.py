# 400. 第 N 位数字
# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。

class Solution:
    def findNthDigit(self, n: int) -> int:
        count = 1
        ind = n
        start = 0
        end = 9

        while ind>(end-start)*count:
            ind-=(end-start)*count
            start=end
            end=end*10+9
            count+=1
        diff,indx = divmod(ind-1,count)
        return int(str(start+diff+1)[indx])

sol = Solution()
print(sol.findNthDigit(3))
