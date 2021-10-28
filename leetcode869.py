# 869. 重新排序得到 2 的幂
# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reordered-power-of-2
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#超时,回溯+哈希
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        MAX_I = 10**9
        targetSet = set()
        for i in range(100):
            tmp = 2**i
            if tmp>MAX_I:
                break
            targetSet.add(tmp)
        nums = list((int(i) for i in str(n)))
        visited = set()
        res = set()
        def backtrack(curr):
            if len(visited)==len(nums):
                res.add(curr in targetSet)
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                if len(visited)==0 and nums[i]==0:
                    continue
                visited.add(i)
                curr=curr*10+nums[i]
                backtrack(curr)
                visited.remove(i)
                curr=(curr-nums[i])//10
        backtrack(0)
        return True in res

# 字典树+回溯
class Solution2:
    def reorderedPowerOf2(self, n: int) -> bool:
        MAX_I = 10**9
        preTree = dict()
        for i in range(100):
            tmp = 2**i
            if tmp>MAX_I:
                break
            self.addTree(preTree,tmp)
        nums = list(str(n))
        visited = set()
        res = set()
        def backtrack(tree):
            if len(visited)==len(nums):
                if 'isEnd' in tree:
                    return True
                return False
            for i in range(len(nums)):
                if i in visited:
                    continue
                if nums[i] not in tree:
                    continue
                visited.add(i)
                if backtrack(tree[nums[i]]):
                    return True
                visited.remove(i)
            return False
        return backtrack(preTree)
        
    
    def addTree(self, tree, num):
        tmp = tree
        for char in str(num):
            if char not in tmp:
                tmp[char]=dict()
            tmp=tmp[char]
        tmp['isEnd']=True

# 回溯+哈希        
class Solution3:
    def reorderedPowerOf2(self, n: int) -> bool:
        MAX_I = 10**9
        targetSet = set()
        for i in range(100):
            tmp = 2**i
            if tmp>MAX_I:
                break
            targetSet.add(tmp)
        nums = list((int(i) for i in str(n)))
        visited = set()
        def backtrack(curr):
            if len(visited)==len(nums):
                return curr in targetSet
            for i in range(len(nums)):
                if i in visited:
                    continue
                if len(visited)==0 and nums[i]==0:
                    continue
                visited.add(i)
                if backtrack(curr*10+nums[i]):
                    return True
                visited.remove(i)
            return False
        return backtrack(0)

# 词频统计        
class Solution4:
    def reorderedPowerOf2(self, n: int) -> bool:
        MAX_I = 10**9
        targetSet = set()
        for i in range(100):
            tmp = 2**i
            if tmp>MAX_I:
                break
            targetSet.add(tuple(sorted(str(tmp))))
        return tuple(sorted(str(n))) in targetSet        

sol = Solution4()
n=12
print(sol.reorderedPowerOf2(n))
