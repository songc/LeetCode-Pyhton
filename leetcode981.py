# 981. 基于时间的键值存储
# 创建一个基于时间的键值存储类 TimeMap，它支持下面两个操作：

# 1. set(string key, string value, int timestamp)

# 存储键 key、值 value，以及给定的时间戳 timestamp。
# 2. get(string key, int timestamp)

# 返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp。
# 如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
# 如果没有值，则返回空字符串（""）。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/time-based-key-value-store
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.collection = collections.defaultdict(dict)
        self.keyTimestamp = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.collection[key][timestamp]=value
        if key not in self.keyTimestamp:
            self.keyTimestamp[key].append(timestamp)
        else:
            bisect.insort_right(self.keyTimestamp[key],timestamp)



    def get(self, key: str, timestamp: int) -> str:
        if key not in self.collection:
            return ""
        if timestamp in self.collection[key]:
            return self.collection[key][timestamp]
        timestampList = self.keyTimestamp[key]
        n = len(timestampList)
        ind = bisect.bisect_right(timestampList, timestamp)
        if ind == 0:
            return ""
        return self.collection[key][timestampList[ind-1]]
        



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("low","high",10)
obj.set("low","high",10)
param_2 = obj.get(key,timestamp)