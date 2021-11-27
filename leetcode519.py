# 519. 随机翻转矩阵
# 给你一个 m x n 的二元矩阵 matrix ，且所有值被初始化为 0 。请你设计一个算法，随机选取一个满足 matrix[i][j] == 0 的下标 (i, j) ，并将它的值变为 1 。所有满足 matrix[i][j] == 0 的下标 (i, j) 被选取的概率应当均等。

# 尽量最少调用内置的随机函数，并且优化时间和空间复杂度。

# 实现 Solution 类：

# Solution(int m, int n) 使用二元矩阵的大小 m 和 n 初始化该对象
# int[] flip() 返回一个满足 matrix[i][j] == 0 的随机下标 [i, j] ，并将其对应格子中的值变为 1
# void reset() 将矩阵中所有的值重置为 0

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/random-flip-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import random
import bisect
from typing import List

class Solution:

    def __init__(self, m: int, n: int):
        self.visited = []
        self.maxInd = m*n-1
        self.m=m
        self.n=n
        


    def flip(self) -> List[int]:
        nextInd = random.randint(0,self.maxInd-len(self.visited))
        ind = bisect.bisect_right(self.visited,nextInd)
        relInd = nextInd+ind
        tmpInd = bisect.bisect_right(self.visited,relInd)
        while ind != tmpInd:
            relInd = nextInd+tmpInd
            ind = tmpInd
            tmpInd = bisect.bisect_right(self.visited,relInd)
        self.visited.insert(tmpInd,relInd)
        m,n = divmod(relInd,self.n)
        return [m,n]



    def reset(self) -> None:
        self.visited=[]



class Solution2:

    def __init__(self, m: int, n: int):
        self.map = dict()
        self.maxInd = m*n-1
        self.m=m
        self.n=n
        


    def flip(self) -> List[int]:
        x = random.randint(0,self.maxInd)
        idx = self.map.get(x,x)
        self.map[x]=self.map.get(self.maxInd,self.maxInd)
        self.maxInd-=1
        m,n = divmod(idx,self.n)
        return [m,n]
        

    def reset(self) -> None:
        self.map=dict()
        self.maxInd=self.m*self.n-1
# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()