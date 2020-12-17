#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

from typing import List

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = [0]
        for ch in s:
            ch_idx = ord(ch) - ord('a')
            if lines[-1] + widths[ch_idx] > 100:
                lines.append(widths[ch_idx])
            else:
                lines[-1] += widths[ch_idx]
        return [len(lines), lines[-1]]

# @lc code=end

