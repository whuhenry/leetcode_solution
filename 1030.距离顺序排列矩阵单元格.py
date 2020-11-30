#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

from typing import List

# @lc code=start
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = []
        for i in range(R):
            for j in range(C):
                result.append([abs(i - r0) + abs(j - c0), [i, j]])
        result.sort(key=lambda item: item[0])
        result = [item[1] for item in result]
        return result
# @lc code=end

