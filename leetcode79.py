# 79. 单词搜索
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
class Solution:
    def exist(self, board: list, word: str) -> bool:
        m,n = len(board),len(board[0])
        visited = set()
        charDict = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                charDict[board[i][j]].append([i,j])
        def dfs(i,j,targetStr,ind):
            m,n = len(board),len(board[0])
            if ind>=len(targetStr):
                return True
            s = targetStr[ind]
            indXY = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for x,y in indXY:
                if x>=0 and x<m and y>=0 and y<n:
                    if  (x,y) not in visited and board[x][y] == s:
                        visited.add((x,y))
                        ans = dfs(x,y,targetStr,ind+1)
                        if ans:
                            return ans
                        visited.remove((x,y))
            return False
        for i,j in charDict[word[0]]:
            visited.add((i,j))
            ans = dfs(i,j,word,1)
            if ans:
                return ans
            visited.remove((i,j))
        return False

sol = Solution()
board =[["a","b"],["c","d"]]


word = "cdba"
print(sol.exist(board,word))