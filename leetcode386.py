# 386. 字典序排数
# 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。

# 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。


from typing import List


# 递归，有额外的空间复杂度
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n<=9:
            return list(range(1,n+1))
        ans = []
        start = 1
        def dfs(start, target):
            for i in range(10):
                nstart = start*10+i
                if nstart>target:
                    return
                ans.append(nstart)
                dfs(nstart,target)
        for i in range(1,10):
            ans.append(i)
            dfs(i,n)
        return ans


class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        num = 1
        for i in range(n):
            ans.append(num)
            if num*10<=n:
                num*=10
            else:
                while num%10==9 or num+1>n:
                    num//=10
                num+=1
        return ans





sol = Solution()
print(sol.lexicalOrder(2345))
        

