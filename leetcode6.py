class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        tlist = [[] for i in range(numRows)]
        i = 0
        step = 1
        for char in s:
            tlist[i].append(char)
            i +=step
            if i== numRows-1:
                step=-1
            if i== 0:
                step=1
        return "".join(["".join(x) for x in tlist ])

s = Solution()
strings = "LEETCODEISHIRING"
numRows = 3
print(s.convert(strings,numRows))
