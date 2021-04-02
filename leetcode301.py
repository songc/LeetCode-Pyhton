# 301. 删除无效的括号
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

# 返回所有可能的结果。答案可以按 任意顺序 返回。
from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans=[]
        tmpSet = set()
        tmpSet.add(s)
        while True:
            for tmp in tmpSet:
                if self.isValid(tmp):
                    ans.append(tmp)
            if ans:
                return ans
            nextTmpSet = set()
            for tmp in tmpSet:
                for i in range(len(tmp)):
                    if tmp[i]=="(" or tmp[i]==")":
                        nextTmpSet.add(tmp[:i]+tmp[i+1:])
            tmpSet = nextTmpSet
        


    def isValid(self, s:str) -> bool:
        cnt = 0
        for char in s:
            if char=="(":
                cnt+=1
            elif char==")":
                cnt-=1
            if cnt<0:
                return False
        return cnt==0

sol = Solution()
# s = "()())()"
s=")("
print(sol.removeInvalidParentheses(s))

        
        

            