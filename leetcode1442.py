# 1442. 形成两个异或相等数组的三元组数目
# 给你一个整数数组 arr 。
# 现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。
# a 和 b 定义如下：
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# 注意：^ 表示 按位异或 操作。
# 请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preXro = [0]
        for a in arr:
            preXro.append(preXro[-1]^a)
        ans = 0
        n = len(preXro)-1
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j,n):
                    a = preXro[i]^preXro[j]
                    b = preXro[k+1]^preXro[j]
                    if a == b:
                        ans+=1
        return ans

class Solution2:
    def countTriplets(self, arr: List[int]) -> int:
        preXro = [0]
        for a in arr:
            preXro.append(preXro[-1]^a)
        ans = 0
        n = len(preXro)-1
        for i in range(n):
            for k in range(i+1,n):
                if preXro[i]==preXro[k+1]:
                    ans+=k-i
        return ans
sol = Solution2()
arr = [1,1,1,1,1]
print(sol.countTriplets(arr))

                