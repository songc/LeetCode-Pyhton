# 88. 合并两个有序数组
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind = 0
        for n2 in nums2:
            while ind<m:
                if n2<nums1[ind]:
                    break
                ind+=1
            nums1.insert(ind,n2)
            nums1.pop()
            m+=1
            ind+=1

# 从后面合并
class Solution2:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind=len(nums1)-1
        ind1 = m-1
        ind2 = n-1
        cur = None
        while ind2>=0 or ind1>=0:
            if ind1==-1:
                cur = nums2[ind2]
                ind2-=1
            elif ind2 == -1:
                cur = nums1[ind1]
                ind1-=1
            elif nums2[ind2]>nums1[ind1]:
                cur=nums2[ind2]
                ind2-=1
            else:
                cur=nums1[ind1]
                ind1-=1
            nums1[ind]=cur
            ind-=1
        

        

