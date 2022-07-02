# 241. 为运算表达式设计优先级
# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。

# 生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/different-ways-to-add-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from ast import operator
from cmath import exp
from functools import lru_cache
from typing import List



class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expe = self.analy(expression)

        @lru_cache(None)
        def dfs(l,r):
            if l==r:
                return [expe[l]]
            res=[]
            for i in range(l,r,2):
                left = dfs(l,i)
                right = dfs(i+2,r)
                for x in left:
                    for y in right:
                        if expe[i+1]=="*":
                            res.append(x*y)
                        elif expe[i+1]=="+":
                            res.append(x+y)
                        elif expe[i+1]=="-":
                            res.append(x-y)
            return res
        return dfs(0,len(expe)-1)


    
    def analy(self,expression:str):
        ans = []
        tmp=0
        for i in expression:
            if i=="*":
                ans.append(tmp)
                tmp=0
                ans.append("*")
            elif i=="+":
                ans.append(tmp)
                tmp=0
                ans.append("+")
            elif i=="-":
                ans.append(tmp)
                tmp=0
                ans.append("-")
            else:
                tmp=tmp*10+int(i)
        ans.append(tmp)
        return ans

sol = Solution()
expression = "2-1-1"
print(sol.diffWaysToCompute(expression))
