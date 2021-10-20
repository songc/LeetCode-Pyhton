# 211. 添加与搜索单词 - 数据结构设计
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

# 实现词典类 WordDictionary ：

# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/design-add-and-search-words-data-structure
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class WordDictionary:

    def __init__(self):
        self.cnt=dict()


    def addWord(self, word: str) -> None:
        tmp = self.cnt
        n = len(word)
        for i in range(n):
            if word[i] not in tmp:
                tmp[word[i]]=dict()
            tmp=tmp[word[i]]
        tmp["flag"]=True


    def search(self, word: str) -> bool:
        
        def bfs(word,wordDict:dict):
            n = len(word)
            tmp =wordDict
            for i in range(n):
                if word[i]==".":
                    flag=False
                    for k in tmp.keys():
                        if k=="flag":
                            continue
                        flag = bfs(word[i+1:],tmp[k])
                        if flag:
                            return flag
                    return flag
                elif word[i] in tmp:
                    tmp=tmp[word[i]]
                else:
                    return False
            if "flag" in tmp:
                return tmp["flag"]
            else:
                return False
        return bfs(word,self.cnt)




# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
param_2 = obj.search(".a")
param_2 = obj.search("a.")