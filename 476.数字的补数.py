#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        bits = []
        while num > 0:
            bits.append((1 + num % 2) % 2)
            num = num // 2
        result = 0
        bits = bits[::-1]
        for bit in bits:
            result = result * 2 + bit
        return result
            
# @lc code=end

s = Solution()
print(s.findComplement(6))