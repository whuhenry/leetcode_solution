#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != sorted_h[i]:
                result += 1
        return result
# @lc code=end

