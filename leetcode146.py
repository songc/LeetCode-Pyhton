# 146. LRU 缓存机制
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 实现 LRUCache 类：

# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#  

# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lru-cache
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections 
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.content = collections.OrderedDict()


    def get(self, key: int) -> int:
        if key in self.content:
            self.content.move_to_end(key)
            return self.content[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.content:
            self.content.move_to_end(key)
            self.content[key]=value
        else:
            if len(self.content)>=self.cap:
                self.content.popitem(False)
            self.content[key]=value

lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
lru.get(1)
lru.put(3,3)
lru.get(2)

