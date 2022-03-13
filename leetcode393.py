# 393. UTF-8 编码验证

# 给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。

# UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

# 对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
# 对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
# 这是 UTF-8 编码的工作方式：

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/utf-8-validation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        num1 = 128
        num2 = 2**7+2**6
        num3 = num2+2**5
        num4 = num3+2**4
        num5 = num4+2**3
        num = 2**7
        n = len(data)
        step = 0
        for i in range(n):
            if step:
                if data[i]&num==num and data[i]&num2==num:
                    step-=1
                else:
                    return False
            else:
                if data[i]&num4==num4 and data[i]&num5==num4:
                    step=3
                elif data[i]&num3==num3:
                    step=2
                elif data[i]&num2==num2:
                    step=1
                elif data[i]<num1:
                    step=0
                else:
                    return False
        return True if step==0 else False
            

sol = Solution()
data = [240,162,138,147]
print(sol.validUtf8(data))
            
        