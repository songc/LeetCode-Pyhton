# 1200. 最小绝对差
# 给你个整数数组 arr，其中每个元素都 不相同。

# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minAbs = 10**7
        ans = []
        arr.sort()
        for i in range(len(arr)-1):
            tmpabs = arr[i+1]-arr[i]
            if tmpabs<minAbs:
                minAbs=tmpabs
                ans.clear()
                ans.append([arr[i],arr[i+1]])
            elif tmpabs==minAbs:
                ans.append([arr[i],arr[i+1]])
        return ans
            