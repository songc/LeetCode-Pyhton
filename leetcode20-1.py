class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n==0 or n%2==1:
            return False
        tmp = []
        dictT = dict([(")","("),("]","["),("}","{")])
        for char in s:
            if char in dictT:
                if tmp and dictT[char] == tmp[-1]:
                    tmp.pop()
                    continue
                else:
                    return False
            tmp.append(char)
        return False if len(tmp)>0 else True