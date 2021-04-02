
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        deque = collections.deque()
        if root is None:
           return True
        deque.append(root.left)
        deque.append(root.right)
        while deque:
            node1 = deque.popleft()
            node2 = deque.popleft()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    deque.append(node1.left)
                    deque.append(node2.right)
                    deque.append(node1.right)
                    deque.append(node2.left)
            elif node1 or node2:
                return False
        return True

             