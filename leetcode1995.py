# 1995. 统计特殊四元组
# 给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：

# nums[a] + nums[b] + nums[c] == nums[d] ，且
# a < b < c < d

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-special-quadruplets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List

#枚举
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    for m in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]==nums[m]:
                            res+=1
        return res

#哈希
class Solution2:
    def countQuadruplets(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n-3):
            for j in range(i+1,n-2):
                tmp=collections.defaultdict(int)
                temp = nums[i]+nums[j]
                for k in range(n-1,j,-1):
                    target = temp+nums[k]
                    if  target in tmp:
                        res+=tmp[target]
                    tmp[nums[k]]+=1
        return res

#哈希+倒序遍历
class Solution3:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        vDict = collections.defaultdict(int)
        for k in range(n-1,1,-1):
            for i in range(k-1):
                for j in range(i+1,k):
                    target = nums[i]+nums[j]+nums[k]
                    if target in vDict:
                        res+=vDict[target]
            vDict[nums[k]]+=1
        return res



sol = Solution3()
nums = [1,2,3,6]
print(sol.countQuadruplets(nums))