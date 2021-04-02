# 341. 扁平化嵌套列表迭代器
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.iterator = None
        self.ind = 0
    
    def next(self) -> int:
        if self.ind<len(self.iterator):
            self.ind+=1
            return self.iterator[self.ind-1]

    def hasNext(self) -> bool:
        if self.iterator is None:
            self.getIterator()
        return self.ind<len(self.iterator)

    def getIterator(self):
        ans = []
        def dfs(nestedList):
            for nested in nestedList:
                if nested.isInteger():
                    ans.append(nested.getInteger())
                else:
                    dfs(nested.getList())
        dfs(self.nestedList)
        self.iterator=ans

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())