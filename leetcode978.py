# 978. 最长湍流子数组
# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

# 返回 A 的最大湍流子数组的长度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-turbulent-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def maxTurbulenceSize(self, arr: list) -> int:
        if len(arr)<=1:
            return len(arr)
        ans = 0
        flag = None
        begin = end = 0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                if flag is None:
                    flag = 1
                elif flag == 1:
                    ans = max(end-begin+1,ans)
                    begin=i
                elif flag == 0:
                    flag=1
            elif arr[i]<arr[i+1]:
                if flag is None:
                    flag = 0
                elif flag==1:
                    flag = 0
                elif flag == 0:
                    ans = max(end-begin+1,ans)
                    begin=i
            else:
                ans = max(end-begin+1,ans)
                begin = i+1
            end+=1
        ans = max(end-begin+1,ans)
        return ans
            
sol = Solution()
arr=[0,8,45,88,48,68,28,55,17,24]
print(sol.maxTurbulenceSize(arr))