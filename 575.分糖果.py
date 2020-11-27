#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

from typing import List

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candySet = set(candyType)
        return min(len(candyType) // 2, len(candySet))
# @lc code=end

