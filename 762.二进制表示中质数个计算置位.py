#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        result = 0
        for num in range(L, R + 1):
            n = num
            count1 = 0
            while n > 0:
                if n % 2 == 1:
                    count1 += 1
                n = n >> 1
            if count1 in prime:
                result += 1
        return result
# @lc code=end

