class Solution:
    def reverse(self, x: int) -> int:
        res=0
        if x>=0:
            temp = [char for char in str(x)]
            temp.reverse()
            res = int("".join(temp))
            return res if res<2**31 else 0
        if x<0:
            temp = [char for char in str(-x)]
            temp.reverse()
            res = int("".join(temp))
            return -res if res < 2**31+1 else 0

S = Solution()
print(S.reverse(123))