# 91. 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

# 题目数据保证答案肯定是一个 32 位 的整数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 递归超时
class Solution:
    def numDecodings(self, s: str) -> int:
        def backtract(s,begin):
            if begin==len(s):
                return 1
            if s[begin]=="0":
                return 0
            one = 0
            two = 0
            one = backtract(s,begin+1)
            if begin+1<len(s) and int(s[begin:begin+2])<=26:
                two = backtract(s,begin+2)
            return one+two
        return backtract(s,0)

class Solution2:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        dp = [1,1]
        n = len(s)
        for i in range(1,n):
            if s[i]=="0":
                if 0<int(s[i-1:i+1])<=26:
                    dp.append(dp[-2])
                else:
                    dp.append(0)
            elif s[i-1]=="0":
                dp.append(dp[-1])
            elif int(s[i-1:i+1])<=26:
                dp.append(dp[-1]+dp[-2])
            else:
                dp.append(dp[-1])
        return dp[-1]
sol = Solution()
s = "1111111111111101"
print(sol.numDecodings(s))
                