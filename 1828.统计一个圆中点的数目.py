#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#

from typing import List

# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        anwser = [0] * len(queries)
        for j, q in enumerate(queries, 0):
            for p in points:
                dist = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                if dist <= q[2] ** 2:
                    anwser[j] += 1
        return anwser
# @lc code=end
