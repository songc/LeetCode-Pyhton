# 1414. 和为 K 的最少斐波那契数字数目
# 给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

# 斐波那契数字定义为：

# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
# 数据保证对于给定的 k ，一定能找到可行解。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k==1:
            return 1
        vlist = [1,1]
        vdict = set(vlist)
        nextv = vlist[-1]+vlist[-2]
        while nextv<=k:
            vlist.append(nextv)
            vdict.add(nextv)
            nextv = vlist[-1]+vlist[-2]
        if k in vdict:
            return 1
        if k-nextv in vdict:
            return 2
        return 1+self.findMinFibonacciNumbers(k-vlist[-1])

class Solution2:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k==1:
            return 1
        vlist = [1,1]
        nextv = vlist[-1]+vlist[-2]
        while nextv<=k:
            vlist.append(nextv)
            nextv = vlist[-1]+vlist[-2]
        ans=0
        i = len(vlist)-1
        while k:
            if k>=vlist[i]:
                k-=vlist[i]
                ans+=1
            else:
                i-=1
        return ans

sol = Solution2()
print(sol.findMinFibonacciNumbers(5))
