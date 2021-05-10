# 1482. 制作 m 束花所需的最少天数
# 给你一个整数数组 bloomDay，以及两个整数 m 和 k 。

# 现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。

# 花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。

# 请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k>n:
            return -1
        deque = collections.deque()
        maxList = []
        left=right = 0
        while right<n:
            while deque and deque[-1]<bloomDay[right]:
                deque.pop()
            deque.append(bloomDay[right])
            right+=1
            if right-left==k:
                maxList.append(deque[0])
                if deque[0]==bloomDay[left]:
                    deque.popleft()
                left+=1
        sortList = sorted(maxList)
        def check(limit,target,step):
            i=0
            tmp=0
            while i <len(maxList):
                if maxList[i]<=limit:
                    i+=k
                    tmp+=1
                else:
                    i+=1
            return tmp>=target
        left = 0
        right = len(sortList)
        while left<right:
            mid = left+(right-left)//2
            if check(sortList[mid],m,k):
                right=mid
            else:
                left=mid+1
        return sortList[left]

bloomDay = [1,10,2,9,3,8,4,7,5,6]
m = 4
k = 2
sol = Solution()
print(sol.minDays(bloomDay,m,k))