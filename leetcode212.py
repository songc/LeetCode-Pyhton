# 212. 单词搜索 II
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        dictTree = self.dictTree(words)
        m,n = len(board),len(board[0])
        visited = set()
        loc = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j,tree):
            if 'flag' in tree and tree['flag']:
                res.append(tree['target'])
                tree['flag']=False
            for x,y in loc:
                nexti=i+x
                nextj = j+y
                if 0<=nexti<m and 0<=nextj<n and (nexti,nextj) not in visited and board[nexti][nextj] in tree:
                    visited.add((nexti,nextj))
                    dfs(nexti,nextj,tree[board[nexti][nextj]])
                    visited.remove((nexti,nextj))
        for i in range(m):
            for j in range(n):
                if board[i][j] in dictTree:
                    visited.add((i,j))
                    dfs(i,j,dictTree[board[i][j]])
                    visited.remove((i,j)) 
        return res

    
    def dictTree(self, words: List[str]) -> dict:
        dictTree = dict()
        for word in words:
            tmp = dictTree
            for char in word:
                if char not in tmp:
                    tmp[char]=dict()
                tmp=tmp[char]
            tmp["flag"]=True
            tmp["target"]=word
        return dictTree
                
sol = Solution()
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
board = [["a","b"],["c","d"]]
words = ["abcb"]
print(sol.findWords(board,words))