# 汇总区间
# 给定一个无重复元素的有序整数数组 nums 。

# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/summary-ranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def summaryRanges(self, nums: list) -> list:
        if len(nums)<1:
            return []
        beginEndList=[]
        begin=nums[0]
        end=nums[0]
        for num in nums:
            if num>end+1:
                if begin == end:
                    beginEndList.append(str(begin))
                else:
                    beginEndList.append(str(begin)+"->"+str(end))
                begin = num
                end = num
            else:
                end =num
        if begin == end:
            beginEndList.append(str(begin))
        else:
            beginEndList.append(str(begin)+"->"+str(end))
        return beginEndList

sol = Solution()
nums=[1]
print(sol.summaryRanges(nums))