# 2034. 股票价格波动
# 给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳 和该时间点股票对应的 价格 。

# 不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 更正 前一条错误的记录。

# 请你设计一个算法，实现：

# 更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 更正 之前的错误价格。
# 找到当前记录里 最新股票价格 。最新股票价格 定义为时间戳最晚的股票价格。
# 找到当前记录里股票的 最高价格 。
# 找到当前记录里股票的 最低价格 。
# 请你实现 StockPrice 类：

# StockPrice() 初始化对象，当前无股票价格记录。
# void update(int timestamp, int price) 在时间点 timestamp 更新股票价格为 price 。
# int current() 返回股票 最新价格 。
# int maximum() 返回股票 最高价格 。
# int minimum() 返回股票 最低价格 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/stock-price-fluctuation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections

from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.vdict= dict()
        self.maxTime=0
        self.maxMum=None
        self.minNum=None


    def update(self, timestamp: int, price: int) -> None:
        oldvalue = self.vdict.get(timestamp)
        self.vdict[timestamp]=price
        self.maxTime=max(self.maxTime,timestamp)
        if not self.maxMum or price>self.maxMum:
            self.maxMum=price
        if not self.minNum or price<self.minNum:
            self.minNum=price
        if oldvalue==self.maxMum and price<self.maxMum:
            self.maxMum=max(self.vdict.values())
        if oldvalue == self.minNum and price>self.minNum:
            self.minNum=min(self.vdict.values())


    def current(self) -> int:
        return self.vdict[self.maxTime]


    def maximum(self) -> int:
        return self.maxMum


    def minimum(self) -> int:
        return self.minNum



class StockPrice:

    def __init__(self):
        self.vdict= dict()
        self.prices = SortedList()
        self.maxTime = 0


    def update(self, timestamp: int, price: int) -> None:
        oldvalue = self.vdict.get(timestamp)
        self.vdict[timestamp]=price
        if oldvalue:
            self.prices.remove(oldvalue)
        self.prices.add(price)
        self.maxTime=max(self.maxTime,timestamp)


    def current(self) -> int:
        return self.vdict[self.maxTime]


    def maximum(self) -> int:
        return self.prices[-1]


    def minimum(self) -> int:
        return self.prices[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()