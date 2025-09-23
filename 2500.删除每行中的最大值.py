#
# @lc app=leetcode.cn id=2500 lang=python3
#
# [2500] 删除每行中的最大值
#

# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(map(max, zip(*list(map(sorted, grid)))))
# @lc code=end

