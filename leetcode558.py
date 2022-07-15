# 558. 四叉树交集
# 二进制矩阵中的所有元素不是 0 就是 1 。

# 给你两个四叉树，quadTree1 和 quadTree2。其中 quadTree1 表示一个 n * n 二进制矩阵，而 quadTree2 表示另一个 n * n 二进制矩阵。

# 请你返回一个表示 n * n 二进制矩阵的四叉树，它是 quadTree1 和 quadTree2 所表示的两个二进制矩阵进行 按位逻辑或运算 的结果。

# 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。

# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        node = Node()
        node.val = quadTree1.val | quadTree2.val
        if quadTree1.isLeaf and quadTree2.isLeaf:
            node.isLeaf=True
            return node
        node.isLeaf=False
        node.topLeft=self.intersect(self.getChild(quadTree1,1),self.getChild(quadTree2,1))
        node.topRight=self.intersect(self.getChild(quadTree1,2),self.getChild(quadTree2,2))
        node.bottomLeft=self.intersect(self.getChild(quadTree1,3),self.getChild(quadTree2,3))
        node.bottomRight=self.intersect(self.getChild(quadTree1,4),self.getChild(quadTree2,4))
        if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf:
            if node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                return Node(node.topLeft.val,True)
        return node
        

    def getChild(self,quadTree1: 'Node', ind:int) -> 'Node':
        if quadTree1.isLeaf:
            return quadTree1
        if ind==1:
            return quadTree1.topLeft
        if ind==2:
            return quadTree1.topRight
        if ind==3:
            return quadTree1.bottomLeft
        return quadTree1.bottomRight
        