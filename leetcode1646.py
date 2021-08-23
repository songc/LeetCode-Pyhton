# 1646. 获取生成数组中的最大值
# 给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ：

# nums[0] = 0
# nums[1] = 1
# 当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
# 当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]
# 返回生成数组 nums 中的 最大 值。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/get-maximum-in-generated-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        if n==0:
            return 0
        if n==1:
            return 1
        res = 0
        for i in range(2,n+1):
            div,mod = divmod(i,2)
            if mod==0:
                tmp = nums[div]
            else:
                tmp = nums[div]+nums[div+1]
            nums.append(tmp)
            res = max(res,tmp)
        return res

sol = Solution()

print(sol.getMaximumGenerated(7))
            
                