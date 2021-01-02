#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        n = len(s) // 2
        counta, countb = 0, 0
        for i in range(n):
            if s[i] in vowels:
                counta += 1
            if s[i + n] in vowels:
                countb += 1
        return counta == countb
# @lc code=end

