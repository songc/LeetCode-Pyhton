# 384. 打乱数组
# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

# 实现 Solution class:

# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shuffle-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.cnt = nums


    def reset(self) -> List[int]:
        return self.cnt


    def shuffle(self) -> List[int]:
        tmp = list(self.cnt)
        res = []
        while tmp:
            ind = random.randint(0,len(tmp)-1)
            res.append(tmp[ind])
            tmp.pop(ind)
        return res
            

class Solution2:

    def __init__(self, nums: List[int]):
        self.cnt = nums
        self.copy = nums.copy()


    def reset(self) -> List[int]:
        return self.copy


    def shuffle(self) -> List[int]:
        res = self.cnt
        for i in range(len(res)):
            ind = random.randint(i,len(res)-1)
            res[i],res[ind]=res[ind],res[i]
        return res




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()