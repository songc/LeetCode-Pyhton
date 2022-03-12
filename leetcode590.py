# 590. N 叉树的后序遍历
# 给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。

# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# Definition for a Node.

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# 递归
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans= []

        def pOrder(node):
            if not node:
                return
            for chil in node.children:
                pOrder(chil)
            ans.append(node.val)
        pOrder(root)
        return ans

#迭代
import collections
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans= []
        stack=[]
        nextInd = collections.defaultdict(int)
        tmp = root
        while tmp or stack:
            while tmp:
                stack.append(tmp)
                nextInd[tmp]=1
                if not tmp.children:
                    break
                tmp = tmp.children[0]
            node = stack[-1]
            ind = nextInd[node]
            if ind<len(node.children):
                nextInd[node]+=1
                tmp=node.children[ind]
            else:
                stack.pop()
                ans.append(node.val)
                del nextInd[node]
                tmp=None
        return ans
                