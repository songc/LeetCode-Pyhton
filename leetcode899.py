# 899. 有序队列
# 给定一个字符串 s 和一个整数 k 。你可以从 s 的前 k 个字母中选择一个，并把它加到字符串的末尾。

# 返回 在应用上述步骤的任意数量的移动后，字典上最小的字符串 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/orderly-queue
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        deque = collections.deque(s)
        if k == 1:
            ans = s
            for i in range(len(deque)):
                deque.append(deque.popleft())
                ans = min(ans,"".join(deque))
            return ans
        return "".join(sorted(deque))
