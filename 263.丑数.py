#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        
        for i in [2, 3, 5]:
            while num % i == 0:
                num = num // i
        if num > 1:
            return False
        return True
# @lc code=end

