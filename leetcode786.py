# 786. 第 K 个最小的素数分数
# 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。

# 对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。

# 那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/k-th-smallest-prime-fraction
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        vlist=[]
        n = len(arr)
        for i in range(n-1):
            for j in range(i,n):
                if len(vlist)<k:
                    heapq.heappush(vlist,(-arr[i]/arr[j],arr[i],arr[j]))
                else:
                    heapq.heappushpop(vlist,(-arr[i]/arr[j],arr[i],arr[j]))
        return [vlist[0][1],vlist[0][2]]

class Solution2:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        vlist = [(arr[0]/arr[i],0,i) for i in range(1,n)]
        heapq.heapify(vlist)
        for _ in range(k-1):
            v,i,j=heapq.heappop(vlist)
            if i+1<j:
                heapq.heappush(vlist,(arr[i+1]/arr[j],i+1,j))
        _,i,j = heapq.heappop(vlist)
        return [arr[i],arr[j]]

class Solution3:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left=0
        right =1
        while True:
            mid = (left+right)/2
            count=0
            x,y= 0,1
            i=-1
            for j in range(1,n):
                while arr[i+1]/arr[j]<mid:
                    i+=1
                    if arr[i]/arr[j]>x/y:
                        x,y=arr[i],arr[j]
                count+=i+1
            if count==k:
                return [x,y]
            if count<k:
                left=mid
            else:
                right=mid

sol = Solution3()
arr = [1,29,47]
k = 1
print(sol.kthSmallestPrimeFraction(arr,k))
