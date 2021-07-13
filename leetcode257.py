# 275. H 指数 II

# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。

# h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        res = 0
        for i in range(n):
            h = n-i
            if citations[i]>=h:
                res = max(res,h)
        return res

class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        n = len(citations)
        if n ==1 :
            return 1 if citations[0]>=1 else 0
        while left<right:
            mid = left+(right-left)//2
            h = n-mid
            if citations[mid]>=h:
                h2 = n-mid+1
                if citations[mid-1]>=h2:
                    right = mid
                else:
                    return h
            else:
                left = mid+1
        return 0

class Solution3:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n=len(citations)
        right = n-1
        while left<=right:
            mid = left+(right-left)//2
            h = n-mid
            if citations[mid]>=h:
                right=mid-1
            else:
                left = mid+1
        return n-left
sol = Solution2()
citations = [10]
print(sol.hIndex(citations))