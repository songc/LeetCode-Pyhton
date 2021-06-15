# 852. 山脉数组的峰顶索引
# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        res = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[res]:
                res = i
        return res


class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right = 0, len(arr)-1
        while left<right:
            mid = left+(right-left)//2
            if arr[mid]>arr[mid+1]:
                right=mid
            else:
                left=mid+1
        return left

sol = Solution2()
arr = [18,29,38,59,98,100,99,98,90]
print(sol.peakIndexInMountainArray(arr))