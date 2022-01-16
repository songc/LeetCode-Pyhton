# 382. 链表随机节点
# 给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。

# 实现 Solution 类：

# Solution(ListNode head) 使用整数数组初始化对象。
# int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-random-node
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head=head


    def getRandom(self) -> int:
        count=1
        tmp= self.head
        res = 0
        while tmp:
            if random.randrange(0,count)==0:
                res=tmp.val
            count+=1
            tmp=tmp.next
        return res