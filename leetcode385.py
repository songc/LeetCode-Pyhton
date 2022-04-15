# 385. 迷你语法分析器
# 给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。

# 列表中的每个元素只可能是整数或整数嵌套列表

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/mini-parser
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) :
        if s[0] !='[':
            return int(s)
        res = []
        stack = [res]
        flag = 1
        num = 0
        tmp=res
        for i in range(1,len(s)):
            if s[i]=='-':
                flag = -1
            elif s[i]=='[':
                newT = list()
                stack.append(tmp)
                tmp.append(newT)
                tmp=newT
            elif s[i]==']':
                if s[i-1]!=']' and s[i-1]!='[':
                    tmp.append(num*flag)
                tmp=stack.pop()
                num=0
                flag=1
            elif s[i]==',':
                if s[i-1]==']':
                    continue
                tmp.append(num*flag)
                num=0
                flag=1
            else:
                num*=10
                num+=int(s[i])
        return res

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        res = NestedInteger()
        if s[0] !='[':
            res.setInteger(int(s))
            return res
        stack = [res]
        flag = 1
        num = 0
        tmp=res
        for i in range(1,len(s)):
            if s[i]=='-':
                flag = -1
            elif s[i]=='[':
                newT = NestedInteger()
                stack.append(tmp)
                tmp.add(newT)
                tmp=newT
            elif s[i]==']':
                if s[i-1]!=']' and s[i-1]!='[':
                    tmp.add(NestedInteger(num*flag))
                tmp=stack.pop()
                num=0
                flag=1
            elif s[i]==',':
                if s[i-1]==']':
                    continue
                tmp.add(NestedInteger(num*flag))
                num=0
                flag=1
            else:
                num*=10
                num+=int(s[i])
        return res

sol = Solution()
s = "[123,[456,[789]]]"
print(sol.deserialize(s))



                

