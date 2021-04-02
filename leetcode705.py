# 705. 设计哈希集合

# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

# 实现 MyHashSet 类：

# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/design-hashset
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 100007
        self.content = [None]*self.mod


    def add(self, key: int) -> None:
        if self.contains(key):
            return
        ind = key % self.mod
        if not self.content[ind]:
            self.content[ind] = [key]
        else:
            self.content[ind].append(key)


    def remove(self, key: int) -> None:
        ind = key%self.mod
        if not self.content[ind]:
            return
        else:
            try:
                self.content[ind].remove(key)
            except ValueError:
                return


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        ind = key%self.mod
        if not self.content[ind]:
            return False
        else:
            for i in self.content[ind]:
                if i==key:
                    return True
            return False