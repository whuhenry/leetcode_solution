#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        bits = [0] * 32
        if num < 0:
            bits[-1] = 1
        absNum = abs(num)
        idx = 0
        while absNum > 0:
            bits[idx] = absNum % 2
            absNum = absNum >> 1
            idx += 1
        if num < 0:
            for i in range(31):
                bits[i] = (bits[i] + 1) % 2
            bits[0] += 1
            idx = 0
            while bits[idx] > 1 and idx < 30:
                bits[idx + 1] += 1
                bits[idx] = 0
                idx += 1
            if bits[idx] == 2:
                bits[idx] = 0
            
        hex_map = ['0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        result = ''
        for i in range(0, 32, 4):
            bitsum = (bits[i + 3] << 3) + (bits[i + 2] << 2)  + (bits[i + 1] << 1) + bits[i]
            result += hex_map[bitsum]
        result = result[::-1]
        start = 0
        while start < 8 and result[start] == '0':
            start += 1
        if start == 8:
            result = '0'
        else:
            result = result[start:]
        return result
        
# @lc code=end

s = Solution()
print(s.toHex(-2147483648))