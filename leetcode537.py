# 537. 复数乘法
# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：

# 实部 是一个整数，取值范围是 [-100, 100]
# 虚部 也是一个整数，取值范围是 [-100, 100]
# i2 == -1
# 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/complex-number-multiplication
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from curses.ascii import SO


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1str = num1.split("+")
        n2str = num2.split("+")
        a1 = int(n1str[0])
        b1 =int(n1str[1][:-1]) 
        a2 = int(n2str[0])
        b2 = int(n2str[1][:-1])
        ans1 = a1*a2-b2*b1
        ans2 = a1*b2+a2*b1
        # return str(ans1)+"+"+str(ans2)+"i"
        return "{}+{}i".format(ans1,ans2)

sol = Solution()
num1 = "1+-1i"
num2 = "1+-1i"
print(sol.complexNumberMultiply(num1,num2))