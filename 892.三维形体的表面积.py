#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

from typing import List

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    area += grid[i][j] * 4 + 2
                    if i - 1 >= 0 and grid[i - 1][j] > 0:
                        area -= min(grid[i][j], grid[i - 1][j]) * 2
                    if j - 1 >= 0 and grid[i][j - 1] > 0:
                        area -= min(grid[i][j], grid[i][j - 1]) * 2
        return area

# @lc code=end

