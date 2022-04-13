# 380. O(1) 时间插入、删除和获取随机元素
# 实现RandomizedSet 类：

# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import random

class RandomizedSet:

    def __init__(self):
        self.cnt=[]
        self.dict={}


    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val]=len(self.cnt)
        self.cnt.append(val)
        return True
        


    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        ind=self.dict[val]
        self.cnt[ind],self.cnt[len(self.cnt)-1]=self.cnt[len(self.cnt)-1],self.cnt[ind]
        self.dict[self.cnt[ind]]=ind
        del self.dict[val]
        self.cnt.pop()
        return True

    def getRandom(self) -> int:
        ind=random.randint(0,len(self.cnt)-1)
        return self.cnt[ind]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()