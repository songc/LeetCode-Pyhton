# 208. 实现 Trie (前缀树)
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = dict()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.tree
        for w in word:
            if w in tmp:
                tmp = tmp[w]
            else:
                tmp[w]=dict()
                tmp = tmp[w]
        tmp["flag"]=True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.tree
        for w in word:
            if w in tmp:
                tmp=tmp[w]
            else:
                return False
        return "flag" in tmp and tmp["flag"]


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.tree
        for w in prefix:
            if w in tmp:
                tmp=tmp[w]
            else:
                return False
        return True