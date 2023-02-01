#
# @lc app=leetcode.cn id=807 lang=python3
#
# [807] 保持城市天际线
#

from typing import List

# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        max_row = [0] * n
        max_col = [0] * n

        for i in range(n):
            max_row[i] = max(grid[i])
            for j in range(n):
                max_col[i] = max(max_col[i], grid[j][i])

        result = 0

        for i in range(n):
            for j in range(n):
                result += min(max_row[i], max_col[j]) - grid[i][j]
        return result


# @lc code=end

