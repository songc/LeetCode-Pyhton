import collections
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = collections.deque()
        beginEnd=[]
        res = 0
        def combineBeginEnd():
            if len(beginEnd)<=1:
                return
            begin1,end1 = beginEnd[-1]
            begin,end = beginEnd[-2]
            if end==begin1-1:
                beginEnd.pop()
                beginEnd[-1][-1]=end1
            elif begin1==begin-1:
                beginEnd.pop(-2)
                combineBeginEnd()

        for ind,char in enumerate(s):
            if char==")":
                if len(queue)==0:
                    continue 
                elif queue[-1][0]=="(":
                    _,i = queue.pop()
                    beginEnd.append([i,ind])
                    combineBeginEnd()                
            if char=="(":
                queue.append(["(",ind])
        for begin,end in beginEnd:
            res = max([end-begin+1,res])
        return res

sol = Solution()
s = "()(((()(()))))"
print(sol.longestValidParentheses(s))
            

