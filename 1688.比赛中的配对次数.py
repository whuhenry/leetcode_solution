#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#
import math

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1:
            result += n // 2
            n = math.ceil(n / 2)
        return result
# @lc code=end
