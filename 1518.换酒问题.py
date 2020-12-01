#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换酒问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            result += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange

        return result
# @lc code=end

