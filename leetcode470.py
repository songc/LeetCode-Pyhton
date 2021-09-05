# 470. 用 Rand7() 实现 Rand10()
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

# 不要使用系统的 Math.random() 方法。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-rand10-using-rand7
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()
        if a>4 and b<4:
            return rand10()
        else:
            return (a+b)%10+1

class Solution2:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            idx = (a-1)*7+b
            if a*b<=40:
                return 1+(idx-1)%10

class Solution2:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        while a > 6:
            a = rand7()
        b = rand7()
        while b > 5:
            b = rand7()
        if a%2==0:
            return b
        else:
            return 5+b

