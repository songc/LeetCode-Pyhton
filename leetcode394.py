# 394. 字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n= len(s)
        cur = 0 
        while cur<n:
            if s[cur].isdigit():
                num = int(s[cur])
                cur+=1
                while cur<n:
                    if  not s[cur].isdigit():
                        break
                    num = num*10+int(s[cur])
                    cur+=1
                stack.append(num)
            elif s[cur].isalpha():
                str1 = s[cur]
                cur+=1
                while cur<n:
                    if not s[cur].isalpha():
                        break
                    str1 += s[cur]
                    cur+=1
                stack.append(str1)
            elif s[cur] == "[":
                stack.append(s[cur])
                cur +=1
            elif s[cur] == "]":
                str2 = stack.pop()
                while stack[-1]!="[":
                    str2 = stack.pop()+str2
                stack.pop()
                count = stack.pop()
                stack.append(str2*count)
                cur+=1
        return "".join(stack)

sol = Solution()
# s = "3[a]2[bc]"
s = "abc3[cd]xyz"
print(sol.decodeString(s))
            