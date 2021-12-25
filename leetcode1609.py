# 1609. 奇偶树
# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：

# 二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
# 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
# 奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
# 给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/even-odd-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        deque=[root]
        level = 0
        while deque:
            tmp = []
            if level%2==0:
                for node in deque:
                    if node.val%2==0:
                        return False
                    else:
                        if node.left:
                            tmp.append(node.left)
                        if node.right:
                            tmp.append(node.right)
                for i in range(len(tmp)-1):
                    if tmp[i].val<=tmp[i+1].val:
                        return False           
            else:
                for node in deque:
                    if node.val%2!=0:
                        return False
                    else:
                        if node.left:
                            tmp.append(node.left)
                        if node.right:
                            tmp.append(node.right)
                for i in range(len(tmp)-1):
                    if tmp[i].val>=tmp[i+1].val:
                        return False 
            deque=tmp
            level+=1
        return True