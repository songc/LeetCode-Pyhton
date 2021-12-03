# 1005. K 次取反后最大化的数组和
# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：

# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。

# 以这种方式修改数组后，返回数组 可能的最大和 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        alist = []
        blist = []
        for i in nums:
            if i<0:
                blist.append(-i)
            else:
                alist.append(i)
        if k==len(blist):
            return sum(alist)+sum(blist)
        elif k<len(blist):
            blist.sort()
            return sum(alist)+sum(blist[len(blist)-k:])-sum(blist[:len(blist)-k])
        elif k>len(blist):
            if (k-len(blist))%2==0:
                return sum(alist)+sum(blist)
            else:
                return sum(alist)+sum(blist)-2*min(alist+blist)
sol = Solution()
nums = [4,2,3]
k = 1
print(sol.largestSumAfterKNegations(nums,k))

        