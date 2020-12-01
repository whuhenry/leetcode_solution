#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        dist = high - low + 1
        if high % 2 == 0:
            return dist // 2
        else:
            if dist % 2 == 0:
                return dist // 2
            else:
                return dist // 2 + 1
# @lc code=end

