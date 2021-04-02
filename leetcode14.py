class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        i=0
        while True:
            char = None
            for s in strs:
                if i>=len(s):
                   return strs[0][:i]
                if char is None:
                    char=s[i]
                else:
                    if char!=s[i]:
                        return strs[0][:i]
            i+=1