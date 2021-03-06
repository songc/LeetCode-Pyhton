# 517. 超级洗衣机
# 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

# 在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

# 给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-washing-machines
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        res = 0
        div,mod = divmod(sum(machines),len(machines))
        if mod:
            return -1
        preSum = 0
        tmp = 0
        res = max(res,max(machines)-div)
        for i in range(len(machines)):
            preSum+=machines[i]
            tmp+=div
            res = max(res,abs(preSum-tmp))
        return res

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        res = 0
        div,mod = divmod(sum(machines),len(machines))
        if mod:
            return -1
        preSum = 0
        tmp =0
        for i in machines:
            preSum+=i
            tmp+=div
            res = max(abs(preSum-tmp),res,i-div)
        return res


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        res = 0
        div,mod = divmod(sum(machines),len(machines))
        if mod:
            return -1
        diff = 0
        for i in machines:
            i-=div
            diff +=i
            res =max(i,res,abs(diff))
        return res





