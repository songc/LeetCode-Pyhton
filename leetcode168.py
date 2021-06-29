# 168. Excel表列名称
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpList= list(map(chr, range(ord('A'), ord('Z')+1)))
        res = ""
        tmp = columnNumber
        while tmp:
            tmp, ind = divmod(tmp,26)
            res = alpList[ind-1]+res
            if ind == 0:
                tmp=tmp-1
        return res

sol = Solution()
num = 701
print(sol.convertToTitle(num))