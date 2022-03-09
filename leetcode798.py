# 798. 得分最高的最小轮调
# 给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为 [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

# 例如，数组为 nums = [2,4,1,3,0]，我们按 k = 2 进行轮调后，它将变成 [1,3,0,2,4]。这将记为 3 分，因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。
# 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = [0]*n
        for i in range(n):
            low = (i+1)%n
            hight = (i-nums[i]+n+1)%n
            diffs[low]+=1
            diffs[hight]-=1
            if low>hight:
                diffs[0]+=1
        ans = 0
        maxScore = 0
        preSum =0
        for i in range(n):
            preSum+=diffs[i]
            if preSum>maxScore:
                maxScore=preSum
                ans = i
        return ans

sol = Solution()
nums = [2,3,1,4,0]
print(sol.bestRotation(nums))