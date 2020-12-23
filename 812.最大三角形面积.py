#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

from typing import List

# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        count = len(points)
        result = 0
        for i in range(count):
            for j in range(i + 1, count):
                for k in range(j + 1, count):
                    area = abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1])) / 2
                    result = max(result, area)
        return result
# @lc code=end

s = Solution()
print(s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))

