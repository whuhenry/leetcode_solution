#
# @lc app=leetcode.cn id=1689 lang=python3
#
# [1689] 十-二进制数的最少数目
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        return min(map(int, n))
# @lc code=end

