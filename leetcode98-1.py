class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrd(tree):
            if tree is not None:
                inOrd(tree.left)
                if tree.val<=self.pre:
                    self.ans=False
                    return
                self.pre=tree.val
                inOrd(tree.right)
        inOrd(root)
        return self.ans
    
    def __init__(self):
        self.pre = float("-inf")
        self.ans = True
        

t5= TreeNode(5)
t4= TreeNode(3)
root = TreeNode(4,t5,t4)
sol = Solution()
print(sol.isValidBST(root))