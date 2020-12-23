#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

from typing import List

# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        B = []
        for j in range(cols):
            line = []
            for i in range(rows):
                line.append(A[i][j])
            B.append(line)
        return B
        
# @lc code=end

