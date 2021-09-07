# 面试题 17.14. 最小K个数
# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
from typing import List
import heapq
import bisect

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k,arr)


class Solution2:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        res = []
        if k==0:
            return res
        for i in arr:
            if len(res)<k:
                bisect.insort_right(res,i)
                continue
            if res[-1]<i:
                continue
            res.pop()
            bisect.insort_right(res,i)
        return res

class Solution3:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        self.quickSort(arr)
        return arr[:k]


    def quickSort(self, arr: List[int], left=0, right=None):
        if right is None:
            right = len(arr)-1
        if left>=right:
            return
        i,j = left,right
        while i<j:
            while i<j and arr[j]>=arr[left]: j-=1
            while i<j and arr[i]<=arr[left]: i+=1
            arr[i],arr[j] = arr[j],arr[i]
        arr[left], arr[i] = arr[i], arr[left]
        self.quickSort(arr,left,i-1)
        self.quickSort(arr,i+1,right)

class Solution4:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        self.quickSort(arr,k)
        return arr[:k]


    def quickSort(self, arr: List[int], k:int, left=0, right=None):
        if right is None:
            right = len(arr)-1
        if left>=right:
            return
        i,j = left,right
        while i<j:
            while i<j and arr[j]>=arr[left]: j-=1
            while i<j and arr[i]<=arr[left]: i+=1
            arr[i],arr[j] = arr[j],arr[i]
        arr[left], arr[i] = arr[i], arr[left]
        if i>k:
            self.quickSort(arr,k,left,i-1)
        if i<k:
            self.quickSort(arr,k,i+1,right)




sol = Solution4()
arr = [1,3,5,7,2,4,6,8]
k = 4
print(sol.smallestK(arr,k))