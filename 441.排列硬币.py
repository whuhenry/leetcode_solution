#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

import math

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(2 * n + 0.25) - 0.5)
# @lc code=end

