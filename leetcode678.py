# 678. 有效的括号字符串
# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

# 任何左括号 ( 必须有相应的右括号 )。
# 任何右括号 ) 必须有相应的左括号 ( 。
# 左括号 ( 必须在对应的右括号之前 )。
# * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
# 一个空字符串也被视为有效字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parenthesis-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 超时
class Solution:
    def checkValidString(self, s: str) -> bool:
        def backtrack(s,ind,curr):
            if ind==len(s):
                return curr==0
            if curr<0:
                return False
            if s[ind]=="(":
                curr+=1
                res=backtrack(s,ind+1,curr)
            elif s[ind]==")":
                curr-=1
                res=backtrack(s,ind+1,curr)
            else:
                res = backtrack(s,ind+1,curr+1)
                if res:
                    return res
                res = backtrack(s,ind+1,curr)
                if res:
                    return res
                res = backtrack(s,ind+1,curr-1)
            return res
        res = backtrack(s,0,0)
        return res

# 栈
class Solution2:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        asteriskStack = []
        n = len(s)
        for i in range(n):
            if s[i]=="(":
                leftStack.append(i)
            elif s[i]=="*":
                asteriskStack.append(i)
            else:
                if leftStack:
                    leftStack.pop()
                    continue
                if asteriskStack:
                    asteriskStack.pop()
                    continue
                return False
        while leftStack and asteriskStack:
            ind1 = leftStack.pop()
            ind2 = asteriskStack.pop()
            if ind1>ind2:
                return False
        return not leftStack

# 模拟：
class Solution3:
    def checkValidString(self, s: str) -> bool:
        l,r = 0,0
        n = len(s)
        for i in range(n):
            if s[i]=="(":
                l+=1
                r+=1
            elif s[i]==")":
                l-=1
                r-=1
            else:
                l-=1
                r+=1
            l = max(l,0)
            if l>r:
                return False
        return l==0


sol = Solution2()
# s= "(*))"
s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
print(sol.checkValidString(s))
        
