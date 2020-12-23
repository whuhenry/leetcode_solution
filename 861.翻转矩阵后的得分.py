#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#

from typing import List

# @lc code=start
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
        for line in A:
            if line[0] == 0:
                for i in range(len(line)):
                    line[i] = (line[i] + 1) % 2
        
        for col in range(cols):
            count1 = 0
            for row in range(rows):
                count1 += A[row][col]
            if count1 < rows / 2:
                for row in range(rows):
                    A[row][col] = (A[row][col] + 1) % 2
        result = 0
        for line in A:
            line_sum = 0
            for cell in line:
                line_sum = (line_sum << 1) + cell
            result += line_sum
        return result
# @lc code=end

s = Solution()
s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
