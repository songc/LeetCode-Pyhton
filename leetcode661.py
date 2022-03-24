# 661. 图片平滑器
# 图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。

# 每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。

# 如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/image-smoother
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        diff = [(1,1),(1,0),(1,-1),(0,1),(0,0),(0,-1),(-1,1),(-1,0),(-1,-1)]
        m,n = len(img),len(img[0])
        ans=[]
        for i in range(m):
            tmp=[]
            for j in range(n):
                tSum=0
                tCount=0
                for x,y in diff:
                    nx=i+x
                    ny=j+y
                    if 0<=nx<m and 0<=ny<n:
                        tSum+=img[nx][ny]
                        tCount+=1
                tmp.append(tSum//tCount)
            ans.append(tmp)
        return ans

sol = Solution()
img = [[100,200,100],[200,50,200],[100,200,100]]
print(sol.imageSmoother(img))