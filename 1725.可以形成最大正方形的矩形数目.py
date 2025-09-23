#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#

from typing import List

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        count = 0
        for rec in rectangles:
            if min(rec) > maxLen:
                maxLen = min(rec)
                count = 1
            elif min(rec) == maxLen:
                count += 1
        return count

# @lc code=end

