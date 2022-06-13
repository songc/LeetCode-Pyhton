# 1051. 高度检查器
# 学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 非递减 的高度顺序排成一行。

# 排序后的高度情况用整数数组 expected 表示，其中 expected[i] 是预计排在这一行中第 i 位的学生的高度（下标从 0 开始）。

# 给你一个整数数组 heights ，表示 当前学生站位 的高度情况。heights[i] 是这一行中第 i 位学生的高度（下标从 0 开始）。

# 返回满足 heights[i] != expected[i] 的 下标数量 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/height-checker
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from ctypes.wintypes import HGDIOBJ
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        ans=0
        for i,j in zip(heights,target):
            if i!=j:
                ans+=1
        return ans