# 676. 实现一个魔法字典
# 设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

# 实现 MagicDictionary 类：

# MagicDictionary() 初始化对象
# void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
# bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/implement-magic-dictionary
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class MagicDictionary:

    def __init__(self):
        self.cnt=collections.defaultdict(list)


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.cnt[len(word)].append(word)


    def search(self, searchWord: str) -> bool:

        for word in self.cnt[len(searchWord)]:
            diff = 0
            for i,j in zip(word,searchWord):
                if i!=j:
                    diff+=1
                    if diff>=2:
                        continue
            if diff==1:
                return True
        return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)