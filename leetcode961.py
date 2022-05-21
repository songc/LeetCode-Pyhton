# 961. 在长度 2N 的数组中找出重复 N 次的元素
# 给你一个整数数组 nums ，该数组具有以下属性：

# nums.length == 2 * n.
# nums 包含 n + 1 个 不同的 元素
# nums 中恰有一个元素重复 n 次
# 找出并返回重复了 n 次的那个元素。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/n-repeated-element-in-size-2n-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        for n in nums:
            count[n]+=1
            if count[n]>1:
                return n