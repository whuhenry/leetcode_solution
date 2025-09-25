#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        digit = set()
        for c in s:
            if '0' <= c <= '9':
                digit.add(int(c))
        if len(digit) < 2:
            return -1
        return sorted(list(digit))[-2]
        
# @lc code=end

