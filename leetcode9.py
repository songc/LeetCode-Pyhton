class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        if x<10:
            return True
        h = x//10
        temp = []
        temp.append(x%10)
        while(h):
            temp.append(h%10)
            h = h//10
        rx = 0
        while temp:
            rx = rx*10+temp.pop(0)
        return rx==x

s=Solution()
x=121
print(s.isPalindrome(x))


