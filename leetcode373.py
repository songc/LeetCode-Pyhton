# 373. 查找和最小的K对数字
# 给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。

# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import sortedcontainers
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res=[]
        deque = sortedcontainers.SortedList()
        visited = set()
        deque.add((nums1[0]+nums2[0],nums1[0],nums2[0],0,0))
        visited.add((0,0))
        n1,n2 = len(nums1),len(nums2)
        while len(res)<k and deque:
            suma,a,b,ind1,ind2 =deque.pop(0)
            res.append([a,b])
            if ind1+1<n1 and (ind1+1,ind2) not in visited:
                deque.add((nums1[ind1+1]+nums2[ind2],nums1[ind1+1],nums2[ind2],ind1+1,ind2))
                visited.add((ind1+1,ind2))
            if ind2+1<n2 and (ind1,ind2+1) not in visited:
                deque.add((nums1[ind1]+nums2[ind2+1],nums1[ind1],nums2[ind2+1],ind1,ind2+1))
                visited.add((ind1,ind2+1))
        return res


class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        visited = set()
        pq = []
        pq.append((nums1[0]+nums2[0],0,0))
        visited.add((0,0))
        while pq and len(res)<k:
            _,i,j = heapq.heappop(pq)
            res.append([nums1[i],nums2[j]])
            if i+1<len(nums1) and (i+1,j) not in visited:
                heapq.heappush(pq,(nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))
            if j+1<len(nums2) and (i,j+1) not in visited:
                heapq.heappush(pq,(nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))
        return res

sol = Solution2()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(sol.kSmallestPairs(nums1,nums2,k))

