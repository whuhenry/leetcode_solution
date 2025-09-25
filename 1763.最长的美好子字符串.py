#
# @lc app=leetcode.cn id=1763 lang=python3
#
# [1763] 最长的美好子字符串
#

# @lc code=start
class Solution:
    def is_perfect(self, s):
        high_set = set()
        low_set = set()
        for c in s:
            if 'Z' >= c >= 'A':
                high_set.add(c.lower())
            else:
                low_set.add(c)
        return high_set == low_set

    def longestNiceSubstring(self, s: str) -> str:
        re = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if j - i + 1 > len(re) and self.is_perfect(s[i: j + 1]):
                    re = s[i: j + 1]
        return re
    
# @lc code=end

s = Solution()
print(s.longestNiceSubstring("YazaAay"))
