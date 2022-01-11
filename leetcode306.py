# 306. 累加数
# 累加数 是一个字符串，组成它的数字可以形成累加序列。

# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。

# 说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/additive-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num)<3:
            return False
        if len(num)==3:
            return int(num[0])+int(num[1])==int(num[2])

        def backtract(pre,target,ind):
            if ind==len(num):
                return True
            tmp=0
            for i in range(ind,len(num)):
                tmp=tmp*10+int(num[i])
                if i+1<len(num) and num[i+1]=="0":
                    continue
                if tmp>target:
                    return False
                elif tmp==target:
                    return backtract(target,pre+target,i+1)
            return False
        n = len (num)
        a=0
        for i in range(n//2):
            a=a*10+int(num[i])
            b=0
            for j in range(i+1,n//3*2):
                b=b*10+int(num[j])
                if j+1<len(num) and num[j+1]=="0" and num[j]!="0":
                    continue
                if backtract(b,a+b,j+1):
                    return True
                if num[j]=="0" and j-i==1:
                    break
            if num[0]=="0":
                break
        return False

sol = Solution()
num = "199001200"
print(sol.isAdditiveNumber(num))
        
    
