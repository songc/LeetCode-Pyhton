# 1582. 二进制矩阵中的特殊位置
# 给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。

# 特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/special-positions-in-a-binary-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans=[]
        row,col = len(mat),len(mat[0])
        rowSum=[sum(x) for x in mat]
        colSum=[]
        for j in range(col):
            tmp=0
            for i in range(row):
                tmp+=mat[i][j]
            colSum.append(tmp)
        for ind,s in enumerate(rowSum):
            if s==1:
                for i in range(col):
                    if mat[ind][i]==1:
                        if colSum[i]==1:
                            ans.append((ind,i))
                        else:
                            break
        return len(ans)

