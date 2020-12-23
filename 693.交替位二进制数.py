#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = n % 2
        n = n // 2
        while n > 0:
            cur = n % 2
            if cur == pre:
                return False
            pre = cur
            n = n // 2
        return True
# @lc code=end

