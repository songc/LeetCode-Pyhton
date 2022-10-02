# 777. 在LR字符串中交换相邻字符
# 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/swap-adjacent-in-lr-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from collections import Counter, defaultdict

##思路错误
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        ind = 0
        for c in start:
            if c=="X":
                continue
            for i in range(ind,len(end)):
                if end[i]==c:
                    ind=i+1
                    break
                if end[i]!='X' and end[i]!=c:
                    return False
            else:
                return False
        return Counter(start)==Counter(end)


class Solution2:
    def canTransform(self, start: str, end: str) -> bool:
        sdict = defaultdict(int)
        slist = []
        elist = []
        # edict = defaultdict(int)
        for c in "LRX":
            sdict[c]=0
            # edict[c]=0
        for s,e in zip(start,end):
            sdict[s]+=1
            sdict[e]-=1
            if s!='X':
                slist.append(s)
            if e!='X':
                elist.append(e)
            if sdict['R']+sdict['X']<0 or sdict['L']+sdict['X']>0:
                return False
        return slist == elist
            
        


sol = Solution2()
start = "RXXLRXRXL"
end = "XRLXXRRLX"
print(sol.canTransform(start,end))