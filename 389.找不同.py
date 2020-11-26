#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = [0 for i in range(26)]
        t_count = [0 for i in range(26)]
        for ch in s:
            s_count[ord(ch) - ord('a')] += 1
        for ch in t:
            t_count[ord(ch) - ord('a')] += 1
        for i in range(26):
            if s_count[i] != t_count[i]:
                return chr(i + ord('a'))
# @lc code=end

