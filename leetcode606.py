# 606. 根据二叉树创建字符串

# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-string-from-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans=[]

        def preOrder(node):
            if not node:
                return
            ans.append(str(node.val))
            ans.append("(")
            preOrder(node.left)
            if ans[-1]=="(" and  not node.right:
                ans.pop()
            else:
                ans.append(")")
            if node.right:
                ans.append("(")
                preOrder(node.right)
                ans.append(")")
        preOrder(root)
        return "".join(ans)

