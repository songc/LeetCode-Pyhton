# 390. 消除游戏
# 给定一个从1 到 n 排序的整数列表。
# 首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
# 第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
# 我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
# 返回长度为 n 的列表中，最后剩下的数字。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/elimination-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def lastRemaining(self, n: int) -> int:
        cnt=n
        begin,end,step=1,n,1
        k = 0
        while cnt>1:
            if k%2==0:
                begin+=step
                if cnt%2:
                    end-=step
            else:
                if cnt%2:
                    begin+=step
                end-=step
            k+=1
            cnt>>=1
            step<<=1
        return begin

sol = Solution()
print(sol.lastRemaining(9))