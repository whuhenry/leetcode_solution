#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#

from typing import List

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = ['' for i in range(len(s))]
        for i in range(len(s)):
            new_s[indices[i]] = s[i]
        return ''.join(new_s)
# @lc code=end

