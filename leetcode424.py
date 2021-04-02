import collections
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        begin,end = 0,0
        numDict = collections.defaultdict(int)
        n =len(s)
        maxT=0
        while end < n:
            numDict[s[end]]+=1
            maxT=max([maxT,numDict[s[end]]])
            if end-begin+1-maxT>k:
                numDict[s[begin]]-=1
                begin+=1
            end+=1
        return end-begin
            
            


sol = Solution()
s="ABAB"
k = 2
print(sol.characterReplacement(s,k))
