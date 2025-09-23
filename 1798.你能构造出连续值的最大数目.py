#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#
from typing import List
# @lc code=start
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        result = 1
        for coin in coins:
            if coin > result:
                break
            else:
                result += coin
        return result
# @lc code=end

