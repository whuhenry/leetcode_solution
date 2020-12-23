#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

from typing import List
import math

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        for i in range(w, 0, -1):
            if area % i == 0:
                return (area // i, i)
                
# @lc code=end

