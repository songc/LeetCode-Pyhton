# 449. 序列化和反序列化二叉搜索树
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

# 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

# 编码的字符串应尽可能紧凑。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/serialize-and-deserialize-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node. 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        degreeList=[]
        curr = [root]
        while curr:
            nextLev = []
            value = []
            for node in curr:
                if not node:
                    value.append("N")
                    continue
                value.append(str(node.val))
                nextLev.append(node.left)
                nextLev.append(node.right)
            curr=nextLev
            while value and value[-1]=="N":
                value.pop()
            if value:
                degreeList.append(value)
        return "#".join(",".join(i) for i in degreeList)
                

                

        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data=="":
            return None
        valueLev = data.split("#")
        root = TreeNode(int(valueLev[0]))
        curr=[root]
        ind=1
        while ind<len(valueLev):
            valueList = valueLev[ind].split(",")
            nextLev = []
            for value in valueList:
                if value=="N":
                    nextLev.append(None)
                else:
                    nextLev.append(TreeNode(int(value)))
            nInd = 0
            for p in curr:
                if not p:
                    continue
                if nInd<len(nextLev):
                    p.left=nextLev[nInd]
                    nInd+=1
                if nInd<len(nextLev):
                    p.right=nextLev[nInd]
                    nInd+=1
                if nInd==len(nextLev):
                    break
            curr=nextLev
            ind+=1
        return root
            
