#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            n = num
            num = 0
            while n > 0:
                num += n % 10
                n = n // 10

        return num
# @lc code=end

