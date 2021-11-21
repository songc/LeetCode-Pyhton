# 594. 最长和谐子序列
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

# 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

# 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-harmonious-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        vdict = collections.defaultdict(int)
        for i in nums:
            vdict[i]+=1
        res=0
        for key in vdict.keys():
            if key+1 in vdict:
                res=max(vdict[key]+vdict[key+1], res)
        return res

sol = Solution()
nums = [1,3,2,2,5,2,3,7]
print(sol.findLHS(nums))
        