#
# @lc app=leetcode.cn id=2520 lang=python3
#
# [2520] 统计能整除数字的位数
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        src = num
        result = 0
        while num > 0:
            digit = num % 10
            num = num // 10
            if src % digit == 0:
                result += 1
        return result
# @lc code=end

