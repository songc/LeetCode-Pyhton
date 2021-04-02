class Solution:
    def myAtoi(self, s: str) -> int:
        temp=[]
        flag=0
        IntMax = 2**31-1
        IntMin = -2**31
        for char in s:
            if char.isspace() and flag==0:
                continue
            if char=="+" and flag==0:
                flag=1
                continue
            if char=="-" and flag==0:
                flag=2
                continue
            if char.isnumeric():
                temp.append(char)
                if flag==0:
                    flag = 1
                continue
            else:
                break
        if len(temp)<1:
            return 0
        res = int("".join(temp))
        if flag==1:
            return res if res<IntMax else IntMax
        if flag==2:
            return -res if -res>IntMin else IntMin 

s = Solution()
strings = "   +0 123"
print(s.myAtoi(strings))