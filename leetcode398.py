# 398. 随机数索引
# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/random-pick-index
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.cnt = collections.defaultdict(list)
        for i,num in enumerate(nums):
            self.cnt[num].append(i)


    def pick(self, target: int) -> int:
        # n = len(self.cnt[target])
        # ind = random.randint(0,n-1)
        # return self.cnt[target][ind]
        return random.choice(self.cnt[target])



class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def pick(self, target: int) -> int:
        ans=cnt=0
        for i,num in enumerate(self.nums):
            if num==target:
                cnt+=1
                if random.randrange(cnt)==0:
                    ans=i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)