# 297. 二叉树的序列化与反序列化
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        deque=collections.deque()
        deque.append(root)
        ans = []
        while deque:
            node=deque.popleft()
            if node:
                ans.append(str(node.val))
                deque.append(node.left)
                deque.append(node.right)
            else:
                ans.append("No")
        while ans and ans[-1]=="No":
            ans.pop()
        return "+".join(ans)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)<1:
            return None
        datas=collections.deque(data.split("+"))
        root = TreeNode(datas.popleft())
        nodes = collections.deque()
        nodes.append(root)
        while nodes:
            node = nodes.popleft()
            left = None
            right = None
            if datas:
                val = datas.popleft()
                if val =="No":
                    left = None
                else:
                    left = TreeNode(int(val))
                    nodes.append(left)
            if datas:
                val = datas.popleft()
                if val =="No":
                    right = None
                else:
                    right = TreeNode(int(val))
                    nodes.append(right)
            node.left=left
            node.right = right
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))