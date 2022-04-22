#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32
        idx = 0
        while n > 0:
            bits[idx] = n % 2
            n = n >> 1
            idx += 1
        result = 0
        for i in range(32):
            result = (result << 1) + bits[i]
        return result
        
# @lc code=end

s = Solution()
print(s.reverseBits(43261596))