#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

from typing import List

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0 for i in range(n)] for j in range(m)]
        result[0][0] = 1
        if obstacleGrid[0][0] == 1:
            return 0
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                result[0][j] = 0
            else:
                result[0][j] = result[0][j - 1]
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                result[i][0] = 0
            else:
                result[i][0] = result[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                else:
                    result[i][j] = result[i - 1][j] + result[i][j - 1]

        return result[m - 1][n - 1]
# @lc code=end

