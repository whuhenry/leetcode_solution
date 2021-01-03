#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ''
        for ch in s:
            if 'a' <= ch <= 'z' or '0' <= ch <= '9':
                result += ch
        return result == result[::-1]
        
# @lc code=end

