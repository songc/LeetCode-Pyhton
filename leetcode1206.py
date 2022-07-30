# 1206. 设计跳表

# 不使用任何库函数，设计一个 跳表 。

# 跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

# 例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作：


# Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

# 跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

# 了解更多 : https://en.wikipedia.org/wiki/Skip_list

# 在本题中，你的设计应该要包含这些函数：

# bool search(int target) : 返回target是否存在于跳表中。
# void add(int num): 插入一个元素到跳表。
# bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
# 注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/design-skiplist
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from random import randint




Level = 10

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = [None]*Level

class Skiplist:

    def __init__(self):
        self.root=Node(-1)

    def find(self, val):
        res = [None]*Level
        cur = self.root
        for i in range(Level-1,-1,-1):
            while cur.next[i] is not None and cur.next[i].val< val:
                cur = cur.next[i]
            res[i]=cur
        return res


    def search(self, target: int) -> bool:
        nodeList = self.find(target)
        return nodeList[0].next[0] is not None and nodeList[0].next[0].val==target


    def add(self, num: int) -> None:
        nodeList = self.find(num)
        tmp = Node(num)
        for i in range(Level):
            tmp.next[i]=nodeList[i].next[i]
            nodeList[i].next[i]=tmp
            if randint(0,2)%2==0:
                break


    def erase(self, num: int) -> bool:
        nodeList = self.find(num)
        node  = nodeList[0].next[0]
        if node is None or node.val !=num:
            return False
        for i in range(Level):
            if nodeList[i].next[i]== node:
                nodeList[i].next[i]=nodeList[i].next[i].next[i]
        return True
