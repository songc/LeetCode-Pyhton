# 677. 键值映射
# 实现一个 MapSum 类，支持两个方法，insert 和 sum：

# MapSum() 初始化 MapSum 对象
# void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
# int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/map-sum-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class MapSum:

    def __init__(self):
        self.cnt = dict()


    def insert(self, key: str, val: int) -> None:
        tmp = self.cnt
        for i in key:
            if i not in tmp:
                tmp[i]=dict()
            tmp=tmp[i]
        tmp['value']=val
                



    def sum(self, prefix: str) -> int:
        tmp = self.cnt
        for i in prefix:
            if i not in tmp:
                return 0
            else:
                tmp=tmp[i]
        return self.sumTree(tmp)


    
    def sumTree(self, tree:dict) ->int:
        res = 0
        for key in tree:
            if key=='value':
                res+=tree['value']
            else:
                res+=self.sumTree(tree[key])
        return res



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)