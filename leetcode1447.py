# 1447. 最简分数
# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。



from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n):
            for j in range(i+1,n+1):
                if self.isSimple(i,j):
                    ans.append("{}/{}".format(i,j))
        return ans
    
    def isSimple(self,a,b):
        tmp = b%a
        while tmp:
            b=a
            a=tmp
            tmp=b%a
        return a==1

sol = Solution()
print(sol.simplifiedFractions(4))