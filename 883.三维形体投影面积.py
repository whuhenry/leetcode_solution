#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

from typing import List

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        x_height = [0] * n
        y_height = [0] * n
        xy = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] > 0:
                    xy += 1
                    x_height[x] = max(x_height[x], grid[x][y])
                    y_height[y] = max(y_height[y], grid[x][y])
        return xy + sum(x_height) + sum(y_height)
# @lc code=end

