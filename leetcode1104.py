# 1104. 二叉树寻路
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。



# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import bisect

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        nums = [1]
        thred = 10**6
        for i in range(1,thred):
            nums.append(nums[-1]+2**i)
            if nums[-1]>thred:
                break
        ind = bisect.bisect_left(nums,label)
        reLabel = nums[ind]-label+nums[ind-1]+1
        p1 = []
        tmp = label
        while tmp:
            p1.append(tmp)
            tmp=tmp//2
        p2 = []
        while reLabel:
            p2.append(reLabel)
            reLabel = reLabel//2
        res = []
        for i in range(len(p1)):
            if i%2==0:
                res.append(p1[i])
            else:
                res.append(p2[i])
        res.reverse()
        return res

sol = Solution()
print(sol.pathInZigZagTree(26))