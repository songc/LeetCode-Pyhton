# 26. 删除排序数组中的重复项
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# class Solution:
#     def removeDuplicates(self, nums: list) -> int:
#         if len(nums)==0:
#             return 0
#         target=nums[0]
#         i=1
#         while i:
#             if i>=len(nums):
#                 break
#             if nums[i]==target:
#                 nums.pop(i)
#             else:
#                 target=nums[i]
#                 i+=1
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums)<=1:
            return len(nums)
        p,q=0,1
        while q<len(nums):
            if nums[p]!=nums[q]:
                p+=1
                nums[p]=nums[q]
            q+=1
        return p+1
                



sol = Solution()
nums = [0,0,1]
print(sol.removeDuplicates(nums))
print(nums)