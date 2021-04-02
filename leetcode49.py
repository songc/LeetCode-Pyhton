# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
import collections
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        charStrList = []
        ans= []
        for s in strs:
            tmpStr = self.transform(s)
            for ind, charStr in  enumerate(charStrList):
                if tmpStr==charStr:
                    ans[ind].append(s)
                    break
            else:
                charStrList.append(tmpStr)
                ans.append([s])
        return ans
    def transform(self, s:str):
        charDict = collections.defaultdict(int)
        for char in s:
            charDict[char]+=1
        tmpList = [ key+str(charDict[key]) for key in sorted(charDict.keys())]
        return "|".join(tmpList)
