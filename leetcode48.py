# 48. 旋转图像
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-image
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2+1):
            for j in range(i,n-i-1):
                tmp = matrix[i][j]
                matrix[i][j]=matrix[n-j-1][i]
                matrix[n-j-1][i]=matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
                matrix[j][n-i-1]=tmp

sol = Solution()
matrix = [[1]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
print(sol.rotate(matrix))
print(matrix)
        
