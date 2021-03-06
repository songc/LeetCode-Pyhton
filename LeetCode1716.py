# 1716. 计算力扣银行的钱
# Hercy 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。

# 最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。

# 给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from curses.ascii import SO


class Solution:
    def totalMoney(self, n: int) -> int:
        div,mod = divmod(n,7)
        weekMon = 28
        res = 0
        res+=(weekMon+weekMon+7*(div-1))*div//2
        res+=(div+1+div+mod)*mod//2
        return res

sol = Solution()
print(sol.totalMoney(10))