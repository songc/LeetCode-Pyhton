# 148. 排序链表
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

# 进阶：

# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
import bisect
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        deque = collections.deque()
        tmp = head
        while tmp:
            deque.append(tmp)
            tmp = tmp.next
        sortedQue = sorted(deque, key = lambda x:x.val)
        for i in range(len(sorted)-1):
            sortedQue[i].next=sortedQue[i+1]
        sortedQue[-1].next=None
        return sortedQue[0]