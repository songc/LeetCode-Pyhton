# 832. 翻转图像
# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flipping-an-image
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for line in A:
            tmp = []
            for i in range(len(line)-1,-1,-1):
                tmp.append(1^line[i])
            ans.append(tmp)
        return ans

sol = Solution()
A = [[1,1,0],[1,0,1],[0,0,0]]
print(sol.flipAndInvertImage(A))