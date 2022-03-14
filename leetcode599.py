# 599. 两个列表的最小索引总和
# 假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        minSum = len(list1)+len(list2)
        vdict=dict(((j,i) for i,j in enumerate(list1)))
        for i,st in enumerate(list2):
            if i>minSum:
                break
            if st not in vdict:
                continue
            tmpSum = i+vdict[st]
            if tmpSum==minSum:
                ans.append(st)
            elif tmpSum<minSum:
                ans.clear()
                ans.append(st)
                minSum=tmpSum
        return ans

        


sol = Solution()
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(sol.findRestaurant(list1,list2))