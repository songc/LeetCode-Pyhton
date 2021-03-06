# 543. 二叉树的直径
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

#  

# 示例 :
# 给定二叉树

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = []
        def dfs(node):
            if node is None:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            ans.append(l+r)
            return max(l,r)+1
        dfs(root)
        return max(ans)
