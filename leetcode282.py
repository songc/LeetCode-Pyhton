# 282. 给表达式添加运算符
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/expression-add-operators
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)
        def backtrace(cnt,ind, curr, mul):
            if ind == n:
                if curr==target:
                    res.append("".join(cnt))
                return
            signIndx = len(cnt)
            if ind>0:
                cnt.append("")
            val = 0
            for i in range(ind,n):
                if i>ind and num[ind]=="0":
                    break
                val = val*10+int(num[i])
                cnt.append(num[i])
                if ind==0:
                    backtrace(cnt,i+1,val,val)
                else:
                    cnt[signIndx]="+"
                    backtrace(cnt,i+1,curr+val,val)
                    cnt[signIndx]="-"
                    backtrace(cnt,i+1,curr-val,-val)
                    cnt[signIndx]="*"
                    backtrace(cnt,i+1,curr-mul+mul*val,mul*val)
            del cnt[signIndx:]
        backtrace([],0,0,0)
        return res

sol = Solution()
num = "123"
target = 6
print(sol.addOperators(num,target))


    