#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

from typing import List

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    result += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        result -= 1
                    if i + 1 < rows and grid[i + 1][j] == 1:
                        result -= 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        result -= 1
                    if j + 1 < cols and grid[i][j + 1] == 1:
                        result -= 1
        return result

# @lc code=end

