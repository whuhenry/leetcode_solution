#
# @lc app=leetcode.cn id=2351 lang=python3
#
# [2351] 第一个出现两次的字母
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        exist_char = set()
        for ch in s:
            if ch in exist_char:
                return ch
            else:
                exist_char.add(ch)
# @lc code=end

