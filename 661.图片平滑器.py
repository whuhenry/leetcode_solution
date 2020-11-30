#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

from typing import List

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows = len(M)
        cols = len(M[0])
        result = []
        for i in range(rows):
            line = []
            for j in range(cols):                
                count = 0
                neighbor_sum = 0
                for u in range(-1, 2):
                    for v in range(-1, 2):
                        if 0 <= i + u <= rows - 1 and 0 <= j + v <= cols - 1:
                            neighbor_sum += M[i + u][j + v]
                            count += 1
                line.append(neighbor_sum // count)
            result.append(line)
        return result
# @lc code=end

