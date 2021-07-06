# 1418. 点菜展示表
# 给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，其中 customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。

# 请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。

# 注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = dict()
        foods = set()
        for order in orders:
            if order[1] not in tables:
                tables[order[1]] = collections.defaultdict(int)
            tables[order[1]][order[2]]+=1
            foods.add(order[2])
        res = []
        orderFood = sorted(foods)
        res.append(["Table"]+orderFood)
        for key in sorted(tables.keys(),key=lambda x:int(x)):
            tmp = [key]
            for food in orderFood:
                if food in tables[key]:    
                    tmp.append(str(tables[key][food]))
                else:
                    tmp.append("0")
            res.append(tmp)
        return res

sol = Solution()
orders= [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(sol.displayTable(orders))