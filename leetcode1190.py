# 1190. 反转每对括号间的子串
# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 注意，您的结果中 不应 包含任何括号。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                temp = reversed(stack.pop())
                stack[-1] += temp
            else:
                stack[-1].append(c)
        return "".join(stack[0])

sol = Solution()
# s = "(abcd)"
s = "(ed(et(oc))el)"
# s = "a(bcdefghijkl(mno)p)q"
print(sol.reverseParentheses(s))