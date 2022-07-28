# 919. 完全二叉树插入器
# 完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

# 设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

# 实现 CBTInserter 类:

# CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
# CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
# CBTInserter.get_root() 将返回树的头节点。


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/complete-binary-tree-inserter
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = collections.deque()
        self.queue.append(root)
        while self.queue[0].left and self.queue[0].right:
            node = self.queue.popleft()
            self.queue.append(node.left)
            self.queue.append(node.right)


    def insert(self, val: int) -> int:
        tmp = TreeNode(val)
        if self.queue[0].left is None:
            self.queue.append(tmp)
            self.queue[0].left = tmp
            return self.queue[0].val
        if self.queue[0].left != self.queue[-1]:
            self.queue.append(self.queue[0].left)
        parent =  self.queue.popleft()
        parent.right=tmp
        self.queue.append(tmp)
        return  parent.val


    def get_root(self) -> TreeNode:
        return self.root



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()