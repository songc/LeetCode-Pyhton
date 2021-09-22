# 725. 分隔链表
# 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。

# 每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。

# 这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。

# 返回一个由上述 k 部分组成的数组。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/split-linked-list-in-parts
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        tmp = head
        while tmp:
            n+=1
            tmp=tmp.next
        res = []
        div,mod = divmod(n,k)
        tmp = head
        for i in range(k):
            res.append(tmp)
            if i < mod:
                for j in range(div):
                    tmp = tmp.next
                pre = tmp
                tmp=tmp.next
                pre.next=None
                continue
            if i>=mod:
                for j in range(div-1):
                    tmp = tmp.next
                if tmp:
                    pre=tmp
                    tmp=tmp.next
                    pre.next=None
        return res
                


