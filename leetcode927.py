# 927. 三等分
# 给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

# 如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：

# arr[0], arr[1], ..., arr[i] 为第一部分；
# arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
# arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
# 这三个部分所表示的二进制值相等。
# 如果无法做到，就返回 [-1, -1]。

# 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

# 提示：

# 3 <= arr.length <= 3 * 104
# arr[i] 是 0 或 1
#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/three-equal-parts
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        count = sum(arr)
        defAns = [-1,-1]
        if count % 3 !=0:
            return defAns
        left,right=0,0
        num = count//3
        target = 0
        tmp=0
        for i in range(1,len(arr)):
            if arr[-i]==1:
                tmp+=1
                target+=2**(i-1)
            if tmp==num:
                break
        tmpValue = 0
        for i in range(0,len(arr)):
            tmpValue=tmpValue*2+arr[i]
            if tmpValue==target:
                left=i
                break
            if tmpValue>target:
                return defAns
        tmpValue = 0
        for i in range(left+1,len(arr)):
            tmpValue=tmpValue*2+arr[i]
            if tmpValue==target:
                right=i
                break
            if tmpValue>target:
                return defAns
        return [left,right+1]

sol = Solution()
arr = [1,1,0,1,1]

print(sol.threeEqualParts(arr))
         