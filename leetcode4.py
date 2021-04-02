class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        # l3 = nums1+nums2
        # l3.sort()
        # length = len(l3)
        # if length%2==0:
        #     index = length//2
        #     return (l3[index]+l3[index-1])/2.0
        # else:
        #     index = length//2
        #     return l3[index]*1.0
        l1Len = len(nums1)
        l2Len = len(nums2)
        l3Len = l1Len+l2Len
        l3 = []
        if l1Len==0:
            l3 = nums2
        if l2Len == 0:
            l3 = nums1
        if l1Len>0 and l2Len>0:
            ind1 = 0
            ind2 = 0
            while ind1<l1Len or ind2<l2Len:
                if ind1==l1Len:
                    l3.append(nums2[ind2])
                    ind2+=1
                    continue 
                if ind2 == l2Len:
                    l3.append(nums1[ind1])
                    ind1+=1
                    continue
                if nums1[ind1] > nums2[ind2]:
                    l3.append(nums2[ind2])
                    ind2+=1
                else:
                    l3.append(nums1[ind1])
                    ind1+=1
                
        if l3Len%2==0:
            index = l3Len//2
            return (l3[index]+l3[index-1])/2.0
        else:
            index = l3Len//2
            return l3[index]*1.0

s = Solution()
nums1 = [1,3]
nums2 = [2]

print(s.findMedianSortedArrays(nums1,nums2))

