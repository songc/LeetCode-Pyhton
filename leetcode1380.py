# 1380. 矩阵中的幸运数

# 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

# 幸运数是指矩阵中满足同时下列两个条件的元素：

# 在同一行的所有元素中最小
# 在同一列的所有元素中最大

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        vset =set()
        ans = list()
        m,n = len(matrix),len(matrix[0])
        for i in range(n):
            vset.add(max(matrix[k][i] for k in range(m)))
        for i in range(m):
            tmp = min(matrix[i])
            if tmp in vset:
                ans.append(tmp)
        return ans

sol = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(sol.luckyNumbers(matrix))