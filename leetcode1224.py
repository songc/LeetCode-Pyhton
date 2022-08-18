# 1224. 最大相等频率
# 给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：

# 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
# 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-equal-frequency
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        ans = 1
        vdict = collections.defaultdict(int)
        vdict2 = collections.defaultdict(set)
        for i,num in enumerate(nums):
            if vdict[num]>0:
                vdict2[vdict[num]].remove(num)
                if len(vdict2[vdict[num]])==0:
                    del vdict2[vdict[num]]
            vdict[num]+=1
            vdict2[vdict[num]].add(num)
            if len(vdict2)==1:
                if len(vdict)==1 or 1 in vdict2 :
                    ans = i
            elif len(vdict2)==2:
              for v in vdict2:
                if len(vdict2[v])==1:
                    if v==1:
                        ans = i
                    elif vdict[list(vdict2[v])[0]]-1 in vdict2:
                        ans = i
        return ans+1

sol = Solution()
nums = [2,2,1,1,5,3,3,5]
print(sol.maxEqualFreq(nums))
