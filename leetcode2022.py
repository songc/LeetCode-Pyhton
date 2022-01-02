# 2022. 将一维数组转变成二维数组
# 给你一个下标从 0 开始的一维整数数组 original 和两个整数 m 和  n 。你需要使用 original 中 所有 元素创建一个 m 行 n 列的二维数组。

# original 中下标从 0 到 n - 1 （都 包含 ）的元素构成二维数组的第一行，下标从 n 到 2 * n - 1 （都 包含 ）的元素构成二维数组的第二行，依此类推。

# 请你根据上述过程返回一个 m x n 的二维数组。如果无法构成这样的二维数组，请你返回一个空的二维数组。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-1d-array-into-2d-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m*n!=len(original):
            return res
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(original[i*n+j])
            res.append(tmp)
        return res

sol = Solution()
original = [1,2,3,4]
m = 2
n = 2
print(sol.construct2DArray(original,m,n))