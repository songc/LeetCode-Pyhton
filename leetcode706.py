# 706. 设计哈希映射
# 实现 MyHashMap 类：

# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/design-hashmap
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 1000009
        # self.key = [None]*self.mod
        self.val = [None]*self.mod


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.val[key]=value


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.val[key] is not None:
            return self.val[key]
        else:
            return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.val[key]=None