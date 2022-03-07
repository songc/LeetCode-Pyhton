# 504. 七进制数
# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。



class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        ans = []
        tmp = abs(num)
        while tmp:
            ans.append(str(tmp%7))
            tmp//=7
        if num<0:
            ans.append("-")
        return "".join(reversed(ans))

sol = Solution()
num = -100
print(sol.convertToBase7(num))