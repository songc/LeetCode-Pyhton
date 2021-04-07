# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections

def createTreeFromList(nums):
    root = TreeNode(nums[0])
    deque = collections.deque()
    deque.append(root)
    ind = 1
    while deque:
        node = deque.popleft()
        if node and ind<len(nums):
            if nums[ind] is not None:
                node.left = TreeNode(nums[ind])
            deque.append(node.left)
            ind+=1
            if nums[ind] is not None:
                node.right = TreeNode(nums[ind])
            deque.append(node.right)
            ind+=1        
    return root