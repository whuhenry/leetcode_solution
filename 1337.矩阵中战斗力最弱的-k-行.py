#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

from typing import List

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        battle = []
        for i, line in enumerate(mat):
            battle.append([i, sum(line)])
        battle.sort(key=lambda x: (x[1], x[0]))

        return [battle[i][0] for i in range(k)]
# @lc code=end

