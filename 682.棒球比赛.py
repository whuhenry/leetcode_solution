#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#
from typing import List

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for op in ops:
            if op == '+':
                result.append(result[-1] + result[-2])
            elif op == 'D':
                result.append(result[-1] * 2)
            elif op == 'C':
                result.pop()
            else:
                result.append(int(op))
        return sum(result)
# @lc code=end

