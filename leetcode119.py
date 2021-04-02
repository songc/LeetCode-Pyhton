# 119. 杨辉三角 II
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        ans.append([1])
        ans.append([1,1])
        for i in range(2,rowIndex):
            tmp = [1]
            for j in range(1,i):
                tmp.append(ans[-1][j-1][j])
            tmp.append[1]
            ans.append(tmp)
        return ans[rowIndex-1]

