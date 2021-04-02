class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        def getKthElement(nums1, nums2, k):
            index1, index2 = 0, 0
            m, n = len(nums1), len(nums2)
            while(True):
                if index1 == m:
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                if k==1:
                    return min(nums1[index1],nums2[index2])
                newInd1 = min(index1+k//2-1,m-1)
                newInd2 = min(index2+k//2-1,n-1)
                if nums1[newInd1]<=nums2[newInd2]:
                    k-=newInd1-index1+1
                    index1=newInd1+1
                else:
                    k -= newInd2-index2+1
                    index2 = newInd2+1
        m, n = len(nums1),len(nums2)
        if (m+n)%2 == 0:
            k = (m+n)//2
            return (getKthElement(nums1,nums2,k) + getKthElement(nums1,nums2,k+1))/2
        else:
            k = (m+n)//2
            return getKthElement(nums1,nums2,k+1)
                
s = Solution()
nums1 = [1,3]
nums2 = [2]

print(s.findMedianSortedArrays(nums1,nums2))
