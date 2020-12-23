#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        result = ''
        sep = []
        if num < 0:
            result = '-'
            num = -num
        while num > 0:
            sep.append(str(num % 7))
            num = num // 7
        sep = sep[::-1]
        for ch in sep:
            result += ch
        return result

# @lc code=end

