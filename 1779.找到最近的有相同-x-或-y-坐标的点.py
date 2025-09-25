#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

from typing import List

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_d = 100000000
        min_idx = -1
        for idx, p in enumerate(points):
            if p[0] == x or p[1] == y:
                d = abs(p[0] - x) + abs(p[1] - y)
                if d < min_d:
                    min_d = d
                    min_idx = idx
        return min_idx
    
# @lc code=end

s = Solution()
print(s.nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]))