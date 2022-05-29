# 468. 验证IP地址
# 给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的 IP 地址，返回 "Neither" 。

# 有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中 0 <= xi <= 255 且 xi 不能包含 前导零。例如: “192.168.1.1” 、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “192.168@1.1” 为无效IPv4地址。

# 一个有效的IPv6地址 是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中:

# 1 <= xi.length <= 4
# xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。
# 在 xi 中允许前导零。
# 例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7334" 是有效的 IPv6 地址，而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 是无效的 IPv6 地址。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/validate-ip-address
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return "IPv4"
        if self.isIPv6(queryIP):
            return "IPv6"
        return "Neither"
        


    def isIPv4(self, queryIP: str) -> bool:
        ipAddr = queryIP.split(".")
        if len(ipAddr)!=4:
            return False
        for i in ipAddr:
            if not i.isdigit():
                return False
            num = int(i)
            if num<0 or num>255:
                return False
            if i!=str(num):
                return False
        return True
    
    def isIPv6(self, queryIP:str) -> bool:
        ipv6  = queryIP.split(":")
        if len(ipv6)!=8:
            return False
        for i in ipv6:
            if len(i)>4 or len(i)<1:
                return False
            if not i.isalnum():
                return False
            try:
                num = int(i,base=16)
            except:
                return False
        return True

sol = Solution()
queryIP = "01.01.01.01"
print(sol.validIPAddress(queryIP))