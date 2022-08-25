# 658. 找到 K 个最接近的元素
# 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

# 整数 a 比整数 b 更接近 x 需要满足：

# |a - x| < |b - x| 或者
# |a - x| == |b - x| 且 a < b


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-k-closest-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from bisect import bisect_left
import collections
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr,x)
        left,right=ind-1,ind
        ans = []
        for _ in range(k):
            if left<0:
                ans.append(arr[right])
                right+=1
                continue
            if right>=len(arr):
                ans.append(arr[left])
                left-=1
                continue
            tmp = abs(arr[left]-x)-abs(arr[right]-x)
            if tmp>0:
                ans.append(arr[right])
                right+=1
            else:
                ans.append(arr[left])
                left-=1
        ans.sort()
        return ans


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr,x)
        left,right=ind-1,ind
        for _ in range(k):
            if left<0:
                right+=1
                continue
            if right>=len(arr):
                left-=1
                continue
            tmp = abs(arr[left]-x)-abs(arr[right]-x)
            if tmp>0:
                right+=1
            else:
                left-=1
        return arr[left+1:right]
sol = Solution2()
arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
print(sol.findClosestElements(arr,k,x))
