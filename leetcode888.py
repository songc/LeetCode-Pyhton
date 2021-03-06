# 888. 公平的糖果棒交换
# 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。

# 因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

# 返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

# 如果有多个答案，你可以返回其中任何一个。保证答案存在。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fair-candy-swap
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def fairCandySwap(self, A: list, B: list) -> list:
        sumA = sum(A)
        sumB = sum(B)
        setA = set(A)
        setB = set(B)
        if sumA>sumB:
            target = (sumA-sumB)//2
            for b in setB:
                if b+target in setA:
                    return [b+target,b]
        elif sumA==sumB:
            for b in setB:
                if b in setA:
                    return [b,b]
        elif sumA<sumB:
            target = (sumB-sumA)//2
            for a in setA:
                if a+target in setB:
                    return [a,a+target]
sol = Solution()
A = [1,1]
B = [2,2]
print(sol.fairCandySwap(A,B))