class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = []
        strSet = set()
        count = 0
        for char in s:
            while (char in strSet):
                string = tmp.pop(0)
                strSet.remove(string)
            tmp.append(char)
            strSet.add(char)
            if len(tmp)>count:
                count=len(tmp)
        return count

sol = Solution()
s= "abcabbababa"
print(sol.lengthOfLongestSubstring(s))
