#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

from typing import List

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_len = len(mat)
        result = 0
        for i in range(mat_len):
            result += mat[i][i]
            result += mat[i][mat_len - i - 1]
        if mat_len % 2 == 1:
            result -= mat[mat_len // 2][mat_len // 2]
        return result
# @lc code=end

