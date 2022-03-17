# 2044. 统计按位或能得到最大值的子集数目
# 给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。

# 如果数组 a 可以由数组 b 删除一些元素（或不删除）得到，则认为数组 a 是数组 b 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同 。

# 对数组 a 执行 按位或 ，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxTmp = 0
        ans=0

        def backtract(cur, ind):
            nonlocal maxTmp,ans
            if ind==len(nums):
                return
            backtract(cur,ind+1)
            cur|=nums[ind]
            if cur==maxTmp:
                ans+=1
            elif cur>maxTmp:
                maxTmp=cur
                ans=1
            backtract(cur,ind+1)
        backtract(0,0)
        return ans

sol = Solution()
nums = [2,2,2]
print(sol.countMaxOrSubsets(nums))
            
            
            