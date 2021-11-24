# 423. 从英文中重建数字
# 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。


from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        digit = [('zero',0),('eight',8),('two',2),('three',3),('six',6),('seven',7),('five',5),('four',4),('one',1),('nine',9)]
        count = Counter(s)
        res= []
        for num,ind in digit:
            tmpC = Counter(num)
            while all(count[key]>=tmpC[key] for key,_ in tmpC.items()):
                res.append(str(ind))
                count-=tmpC
        return "".join(sorted(res))

sol = Solution()
s = "owoztneoer"
print(sol.originalDigits(s))
