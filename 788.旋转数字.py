#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(1, N + 1):
            str_n = str(i)
            if '3' in str_n or '4' in str_n or '7' in str_n:
                continue
            if '2' in str_n or '5' in str_n or '6' in str_n or '9' in str_n:
                count += 1
        return count
# @lc code=end

