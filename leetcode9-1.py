class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        if x<10:
            return True
        rx=0
        h = x
        while(h):
            rx = rx*10 + h%10
            h = h//10
        return rx==x

s=Solution()
x=121
print(s.isPalindrome(x))