# 839. 相似字符串组
# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。

# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

# 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/similar-string-groups
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def numSimilarGroups(self, strs: list) -> int:
        parent=[i for i in range(len(strs))]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(x)]=find(y)
        for i in range(len(strs)):            
            for j in range(len(strs)):
                if i==j:
                    continue
                diff = 0
                for s1,s2 in zip(strs[i],strs[j]):
                    if s1!=s2:
                        diff+=1
                        if diff>2:
                            break
                if diff<=2:
                    union(i,j)
        vset=set()
        for i in range(len(strs)):
            vset.add(find(i))
        return len(vset)

sol = Solution()
strs=["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]
print(sol.numSimilarGroups(strs))
                

