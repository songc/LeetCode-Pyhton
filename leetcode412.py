# 412. Fizz Buzz
# 写一个程序，输出从 1 到 n 数字的字符串表示。

# 1. 如果 n 是3的倍数，输出“Fizz”；

# 2. 如果 n 是5的倍数，输出“Buzz”；

# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fizz-buzz
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        a,b,c= "Fizz","Buzz", "FizzBuzz"
        for i in range(1,n+1):
            if i%15==0:
                res.append(c)
            elif i%3==0:
                res.append(a)
            elif i%5==0:
                res.append(b)
            else:
                res.append(str(i))
        return res
