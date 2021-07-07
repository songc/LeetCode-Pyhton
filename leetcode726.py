# 726. 原子的数量
# 给定一个化学式formula（作为字符串），返回每种原子的数量。

# 原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

# 两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

# 一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

# 给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-atoms
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        tmp = self.count(formula,0)
        d = tmp[0]
        res = []
        for key in sorted(d.keys()):
            res.append(key)
            if d[key] !=1:
                res.append(str(d[key]))
        return "".join(res)

    def count(self, formula:str, begin:int):
        d = collections.defaultdict(int)
        n = len(formula)
        end = begin
        while begin<n:
            omic = formula[begin]
            num = 1
            if omic.isupper():
                if begin+1<n and formula[begin+1].islower():
                    begin+=1
                    omic+=formula[begin]
                if  begin+1<n and formula[begin+1].isdigit():
                    begin+=1
                    num = int(str(formula[begin]))
                    while begin+1<n and formula[begin+1].isdigit():
                        begin+=1
                        num =num*10+int(str(formula[begin]))
                d[omic]+=num
                
            if omic == "(":
               tmp = self.count(formula, begin+1)
               self.dictUpdate(d,tmp[0])
               begin = tmp[1]
            if omic == ")":
                if  begin+1<n and formula[begin+1].isdigit():
                    begin+=1
                    num = int(str(formula[begin]))
                    while begin+1<n and formula[begin+1].isdigit():
                        begin+=1
                        num =num*10+int(str(formula[begin]))
                self.dictMult(d,num)
                end = begin
                return d,end
            begin+=1
            end = begin
        return d,end
               
    def dictUpdate(self, a, b):
        for key in  b:
            a[key]+=b[key]

    def dictMult(self,b, mult):
        for key in b:
            b[key]*=mult


sol = Solution()
formula = "(H)"
print(sol.countOfAtoms(formula))