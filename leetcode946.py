# 946. 验证栈序列
# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/validate-stack-sequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n=len(pushed)
        ind1,ind2=0,0
        while ind1<n:
            stack.append(pushed[ind1])
            while ind2<n and stack and popped[ind2]==stack[-1]:
                stack.pop()
                ind2+=1
            ind1+=1
        return not stack

sol = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,1,2]
print(sol.validateStackSequences(pushed,popped))