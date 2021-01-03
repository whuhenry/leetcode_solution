#
# @lc app=leetcode.cn id=1525 lang=python3
#
# [1525] 字符串的好分割数目
#

import collections

# @lc code=start
class Solution:
    def numSplits(self, s: str) -> int:
        s_counter = collections.Counter(s)
        left_charset = set()
        result = 0
        for ch in s:
            s_counter[ch] -= 1
            if s_counter[ch] == 0:
                s_counter.pop(ch)
            left_charset.add(ch)
            if len(s_counter) == len(left_charset):
                result += 1
        return result
# @lc code=end

