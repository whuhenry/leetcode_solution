#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        idx = 0
        for ch in s:
            idx = idx * 26 + ord(ch) - ord('A') + 1
        return idx
# @lc code=end

