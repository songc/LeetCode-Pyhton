# 528. 按权重随机选择
# 给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标 i，选取下标 i 的概率与 w[i] 成正比。

# 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。

# 也就是说，选取下标 i 的概率为 w[i] / sum(w) 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/random-pick-with-weight
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import bisect
import random

class Solution:

    def __init__(self, w: List[int]):
        self.cnt = w
        tmp=0
        self.preSum=[]
        for n in self.cnt:
            tmp+=n
            self.preSum.append(tmp)

    def pickIndex(self) -> int:
        i = random.randint(1,self.preSum[-1])
        return bisect.bisect_left(self.preSum,i)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
boj = Solution([1])
print(boj.pickIndex())