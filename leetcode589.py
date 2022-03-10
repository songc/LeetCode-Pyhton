# 589. N 叉树的前序遍历
# 给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。

# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List
import collections

# 递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans
        ans.append(root.val)
        if not root.children:
            return ans
        for chil in root.children:
            tmp = self.preorder(chil)
            ans.extend(tmp)
        return ans


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        stack = []
        if not root:
            return ans
        tmp = root
        nextInd = collections.defaultdict(int)
        while tmp or stack:
            while tmp:
                ans.append(tmp.val)
                stack.append(tmp)
                if not tmp.children:
                    break
                nextInd[tmp]=1
                tmp=tmp.children[0]
            tmp = stack[-1]
            i = nextInd[tmp]
            if i<len(tmp.children):
                nextInd[tmp]=i+1
                tmp=tmp.children[i]
            else:
                stack.pop()
                del nextInd[tmp]
                tmp=None
        return ans
                
