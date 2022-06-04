# 929. 独特的电子邮件地址
# 每个 有效电子邮件地址 都由一个 本地名 和一个 域名 组成，以 '@' 符号分隔。除小写字母之外，电子邮件地址还可以含有一个或多个 '.' 或 '+' 。

# 例如，在 alice@leetcode.com中， alice 是 本地名 ，而 leetcode.com 是 域名 。
# 如果在电子邮件地址的 本地名 部分中的某些字符之间添加句点（'.'），则发往那里的邮件将会转发到本地名中没有点的同一地址。请注意，此规则 不适用于域名 。

# 例如，"alice.z@leetcode.com” 和 “alicez@leetcode.com” 会转发到同一电子邮件地址。
# 如果在 本地名 中添加加号（'+'），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件。同样，此规则 不适用于域名 。

# 例如 m.y+name@email.com 将转发到 my@email.com。
# 可以同时使用这两个规则。

# 给你一个字符串数组 emails，我们会向每个 emails[i] 发送一封电子邮件。返回实际收到邮件的不同地址数目。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/unique-email-addresses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(self.getEmail(email) for email in emails))

    
    def getEmail(self, email:str) -> str:
        strList = email.split("@")
        path = strList[0].split("+")[0].replace(".","")
        return path+"@"+strList[1]

sol = Solution()
emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(sol.numUniqueEmails(emails))