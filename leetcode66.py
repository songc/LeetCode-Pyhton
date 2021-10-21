# 66. 加一
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plus-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num=num*10+i
        num+=1
        return [int(i) for i in str(num)]


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = 0
        res=[]

        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                m,mod = divmod(digits[i]+1+m,10)
            else:
                m,mod = divmod(digits[i]+m,10)
            res.append(mod)
        if m==1:
            res.append(m)
        res.reverse()
        return res

class Solution3:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            digits[i]=0
        res = [0]*(len(digits)+1)
        res[0]=1
        return res

sol = Solution2()
digits = [1,2,3]
print(sol.plusOne(digits))