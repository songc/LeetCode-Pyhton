# 160. 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。
# 注意：

# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tA = headA
        tB = headB
        lenA,lenB = 0,0
        if not headA or not headB:
            return None
        while tA.next or tB.next:
            if tA == tB:
                break
            if tA.next:
                tA = tA.next
                lenA+=1
            if tB.next:
                tB = tB.next
                lenB+=1
        if tA == tB:
            if lenA==lenB:
                return tA
            elif lenA>lenB:
                diff = lenA-lenB
                tA, tB = headA, headB
                while tA:
                    if diff>0:
                        tA=tA.next
                        diff-=1
                    else:
                        if tA == tB:
                            return tA
                        tA=tA.next
                        tB=tB.next
            elif lenA<lenB:
                diff = lenB-lenA
                tA, tB = headA, headB
                while tB:
                    if diff>0:
                        tB=tB.next
                        diff-=1
                    else:
                        if tA == tB:
                            return tA
                        tA=tA.next
                        tB=tB.next
        return None
