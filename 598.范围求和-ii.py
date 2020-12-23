#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

from typing import List

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_a = m
        min_b = n
        for op in ops:
            min_a = min(min_a, op[0])
            min_b = min(min_b, op[1])
        return min_a * min_b
# @lc code=end

