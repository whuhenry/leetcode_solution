#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

from typing import List

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        rows = len(mat)
        cols = len(mat[0])
        for line in mat:
            if sum(line) == 1:
                flag = True
                for j in range(cols):
                    if line[j] == 1:
                        count = 0
                        for i in range(rows):
                            count += mat[i][j]
                            if count > 1:
                                flag = False
                                break
                        break
                if flag:
                    result += 1
        return result
# @lc code=end

