#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split()
        if 0 == len(tmp):
            return 0
        return len(tmp[-1])
# @lc code=end

