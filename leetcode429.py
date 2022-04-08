# 429. N 叉树的层序遍历
# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。


# Definition for a Node.
from socketserver import DatagramRequestHandler


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans
        deque = [root]
        while deque:
            tmp = []
            nextDeque = []
            for node in deque:
                tmp.append(node.val)
                for ch in node.children:
                    nextDeque.append(ch)
            ans.append(tmp)
            deque=nextDeque
        return ans

