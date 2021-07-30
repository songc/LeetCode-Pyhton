# 171. Excel表列序号

# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            res =res*26 + (ord(c)-ord('A')+1)
        return res

sol = Solution()
columnTitle = "FXSHRXW"
print(sol.titleToNumber(columnTitle))
