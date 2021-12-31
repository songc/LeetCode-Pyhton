# 507. 完美数
# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

# 给定一个 整数 n， 如果是完美数，返回 true，否则返回 false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        left=2
        right=num**0.5
        vset=set()
        vset.add(1)
        while left<=right:
            div,mod = divmod(num,left)
            if mod==0:
                vset.add(left)
                vset.add(div)
            left+=1
        return sum(vset)==num



class Solution2:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sumP = 1
        i=2
        while i <= num//i:
            div,mod = divmod(num,i)
            if mod==0:
                sumP+=i
                sumP+=div
            i+=1
        return sumP==num


sol = Solution2()
num = 496
print(sol.checkPerfectNumber(num))
