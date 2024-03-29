# 1460. 通过翻转子数组使两个数组相等
# 给你两个长度相同的整数数组 target 和 arr 。每一步中，你可以选择 arr 的任意 非空子数组 并将它翻转。你可以执行此过程任意次。

# 如果你能让 arr 变得与 target 相同，返回 True；否则，返回 False 。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/make-two-arrays-equal-by-reversing-sub-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target)==Counter(arr)