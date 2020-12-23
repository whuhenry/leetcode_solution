#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

from typing import List

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        result = [[0 for i in range(n)] for j in range(m)]
        for j in range(n):
            times = (j + k) // n
            target_col = (j + k) % n
            target_row = times % m
            idx = 0
            for i in range(target_row, target_row + m):
                row = i % m
                result[row][target_col] = grid[idx][j]
                idx += 1
        return result
# @lc code=end

s = Solution()
print(s.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))