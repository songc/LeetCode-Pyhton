class ListNode:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.content = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key: int) -> int:
        if key in self.content:
            self.move_to_end(key)
            return self.content[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.content:
            self.move_to_end(key)
            self.content[key].val = value
        else:
            if len(self.content)>=self.cap:
                self.removeHead()
            self.addTail(key,value)

    def move_to_end(self,key):
        node = self.content[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
    
    def addTail(self,key,val):
        node = ListNode(key,val)
        node.next = self.tail
        node.pre = self.tail.pre
        self.tail.pre.next = node
        self.tail.pre = node
        self.content[key]=node
    
    def removeHead(self):
        del self.content[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.pre = self.head


lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
lru.get(1)
lru.put(3,3)
lru.get(2)
