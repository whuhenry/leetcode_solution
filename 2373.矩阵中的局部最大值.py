#
# @lc app=leetcode.cn id=2373 lang=python3
#
# [2373] 矩阵中的局部最大值
#
from typing import List

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []
        for i in range(n - 2):
            row_res = []
            for j in range(n - 2):
                row_res.append(max([grid[p][q] for p in range(i, i + 3) for q in range(j, j + 3)]))
            result.append(row_res)
        return result
# @lc code=end

